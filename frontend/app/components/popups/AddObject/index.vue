<script setup>
	import { objectSerializer } from '~/utils/serializers/objectSerializer';
	import oposCategories from '~/assets/oposCategories';

	const { closeCurrentPopup }       = usePopupsStore();
	const clientsStore                = useClientsStore();
	const { addObject: addNewObject } = useObjectsStore();
	const { addToast }                = useToastsStore();
	const { objects }                 = useApi();
	const { requiredField }           = useValidation();

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
	const isNewClient          = ref(false);
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
		newObject.value.oposCategory = oposCategories.filter(category => category.id === id)[0].text;
	};

	const changeIsNewClient = () => isNewClient.value = !isNewClient.value;

	const addObject = async () =>
	{
		const { valid } = await r$.$validate();

		if (!valid)
			return;

		isLoading.value = true;

		try {
			const response = await objects.addObject(newObject.value);

			if (response.object_id)
			{
				addNewObject(objectSerializer(response));
				addToast('Объект добавлен', 'success');
				closeCurrentPopup();
			}
		}
		catch (err) { useRequestError(err) }
		finally { isLoading.value = false; }
	};

	await clientsStore.getClients();
</script>

<template>
	<div class="wrapper">
		<PopupsHeader title="Добавить объект" />

		<div class="content">
			<div class="body" :class="{ 'active': isNewClient }">
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
						:items="oposCategories"
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
				<div class="new-client">
					<input
						type="checkbox"
						id="isNewClient"
						:checked="isNewClient"
						@change="changeIsNewClient"
					/>
					<label for="isNewClient">Новый клиент?</label>
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

			<Transition name="fade-left">
				<PopupsAddObjectClient
					v-if="isNewClient"
					@close="changeIsNewClient"
				/>
			</Transition>
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
		column-gap: 40px;

		display: flex;
	}

	.body
	{
		gap: 20px;

		display: flex;
		position: relative;
		flex-direction: column;

		&.active
		{
			&::before
			{
				width: 1px;
				height: 100%;
				content: '';
				background-color: $light-gray;

				position: absolute;
				right: calc(0% - 20px);
				top: 0;
			}
		}
	}

	.inputs
	{
		gap: 20px;

		display: grid;
		grid-template-columns: repeat(2, 200px);
		grid-template-rows: repeat(2, 1fr);
	}

	.new-client
	{
		column-gap: 10px;

		display: flex;
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