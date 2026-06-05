<script setup>
	const { closeCurrentPopup } = usePopupsStore();
	const clientsStore          = useClientsStore();
	const { objects }           = useApi();
	const { requiredField }     = useValidation();

	const OPOCategories =
	[
		{
			id   : 1,
			text : '1 Класс'
		},
		{
			id   : 2,
			text : "2 Класс"
		},
		{
			id   : 3,
			text : '3 Класс'
		},
		{
			id   : 4,
			text : "4 Класс"
		}
	];

	const newObject = ref(
		{
			clientId      : null,
			objectName    : '',
			objectAddress : '',
			oposCategory  : '',
			description   : ''
		}
	);

	const isLoading            = ref(false);
	const currentClientId      = ref(null);
	const currentOPOCategoryId = ref(null);

	const { r$ } = useRegle(newObject.value, { ...requiredField('clientId', 'Клиент обязателен') });

	const chooseClient = (id) =>
	{
		currentClientId.value    = id;
		newObject.value.clientId = id;
	};

	const chooseOPOCategory = (id) =>
	{
		currentOPOCategoryId.value   = id;
		newObject.value.oposCategory = id;
	};

	const addObject = async () =>
	{
		const { valid } = await r$.$validate();

		if (!valid)
			return;

		isLoading.value = true;

		try {
			const response = await objects.addObject(newObject.value);
			console.log(response);
		}
		catch (err) { useRequestError(err) }
		finally { isLoading.value = false; }
	};

	await clientsStore.getClients();
</script>

<template>
	<div class="wrapper">
		<div class="header">
			<p class="title">Добавить объект</p>
			<IconsClose class="close" @click="closeCurrentPopup" />
		</div>

		<div class="body">
			<div class="inputs">
				<UiInput
					placeholder="Название объекта"
					variant="small"
					v-model="newObject.objectName"
				/>
				<UiInput
					placeholder="Адрес объекта"
					variant="small"
					v-model="newObject.objectAddress"
				/>
				<UiSelect
					:items="clientsStore.clients"
					placeholder="Клиент"
					:currentItemId="currentClientId"
					textFieldName="name"
					@chooseSelectItem="chooseClient"
					:error="r$.$errors.clientId[0]"
				/>
				<UiSelect
					:items="OPOCategories"
					placeholder="Категория ОПО"
					:currentItemId="currentOPOCategoryId"
					textFieldName="text"
					@chooseSelectItem="chooseOPOCategory"
				/>
			</div>
			<UiTextarea
				class="description"
				placeholder="Описание"
				v-model="newObject.description"
			/>
		</div>
		<div class="buttons">
			<UiButton
				variant="green"
				:disabled="isLoading"
				@click="addObject"
			>
				Добавить
			</UiButton>
			<UiButton
				variant="dark"
				@click="closeCurrentPopup"
			>
				Отменить
			</UiButton>
		</div>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		border: 1px solid rgba($green, 0.5);
		padding: 30px;
		border-radius: 15px;
		background-color: $primary;
	}

	.header
	{
		column-gap: 20px;
		margin-bottom: 30px;

		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.title
	{
		font-size: 24px;
		line-height: 100%;
		font-weight: 500;
	}

	.close
	{
		width: 16px;
		height: 16px;
		cursor: pointer;
		color: rgba($red, 0.3);

		@include tr(0.3, color);

		&:hover { color: $red; }
	}

	.body
	{
		gap: 20px;
		margin-bottom: 20px;

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

	.buttons
	{
		column-gap: 20px;

		display: flex;

		button
		{
			width: 100%;
			justify-content: center;
		}
	}
</style>