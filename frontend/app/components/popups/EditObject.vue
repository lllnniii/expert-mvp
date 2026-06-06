<script setup>
	import oposCategories from '~/assets/oposCategories';

	const objectsStore           = useObjectsStore();
	const popupsStore            = usePopupsStore();
	const { addToast }           = useToastsStore();
	const { objects: objectApi } = useApi();

	const objectData = ref(
		{
			id           : popupsStore.popupData.id,
			name         : popupsStore.popupData.name,
			address      : popupsStore.popupData.address,
			description  : popupsStore.popupData.description,
			oposCategory : popupsStore.popupData.oposCategory
		}
	);

	const currentOPOId = ref(null);
	const isLoading    = ref(false);

	currentOPOId.value = oposCategories.find(category => category.text === objectData.value.oposCategory).id;

	const chooseOPOCategory = (id) =>
	{
		const choosedOPOCategory = oposCategories.find(category => category.id === id);

		objectData.value.oposCategory = choosedOPOCategory.text
		currentOPOId.value            = id;
	};

	const changeObject = async () =>
	{
		isLoading.value = true;

		try {
			const response = await objectApi.changeObject(objectData.value);

			if (response.object_id)
			{
				objectsStore.updateObject(response);
				addToast('Объект изменен', 'success');
				popupsStore.closeCurrentPopup();
			}
		}
		catch (err) { useRequestError(err) }
		finally { isLoading.value = false; }
	};
</script>

<template>
	<div class="wrapper">
		<PopupsHeader title="Изменить объект" />

		<div class="content">
			<div class="inputs">
				<UiInput
					variant="small"
					placeholder="Наименование"
					v-model="objectData.name"
				/>
				<UiInput
					variant="small"
					placeholder="Адрес"
					v-model="objectData.address"
				/>
				<UiSelect
					:items="oposCategories"
					:currentItemId="currentOPOId"
					textFieldName="text"
					placeholder="Класс ОПО"
					@chooseSelectItem="chooseOPOCategory"
				/>
			</div>
			<UiTextarea
				placeholder="Описание"
				v-model="objectData.description"
			/>
			<div class="buttons">
				<UiButton
					variant="green"
					:disabled="isLoading"
					@click="changeObject"
				>
					Изменить
				</UiButton>
				<UiButton
					variant="dark"
					@click="popupsStore.closeCurrentPopup"
				>
					Отменить
				</UiButton>
			</div>
		</div>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		border: 1px solid rgba($green, 0.5);
		padding: 30px;
		overflow-x: hidden;
		border-radius: 15px;
		background-color: $primary;
	}

	.content
	{
		row-gap: 20px;

		display: flex;
		flex-direction: column;
	}

	.inputs
	{
		gap: 20px;

		display: grid;
		grid-template-columns: repeat(2, 200px);
		grid-template-rows: repeat(2, 1fr);
	}

	.content .textarea { width: 100%; }

	.buttons
	{
		column-gap: 10px;

		display: flex;

		button
		{
			width: 100%;
			justify-content: center;
		}
	}
</style>