<script setup>
	const { clients }   = useApi();
	const { addClient } = useClientsStore();
	const { addToast }  = useToastsStore();
	const {
		emailField,
		phoneField,
		minLengthField,
		requiredField
	}                   = useValidation();

	const newClient = ref(
		{
			inn           : '',
			fullName      : '',
			clientName    : '',
			contactEmail  : '',
			contactPhone  : '',
			addressLegal  : '',
			addressActual : '',
			contactPerson : ''
		}
	);

	const { r$ } = useRegle(
		newClient.value,
		{
			...phoneField('contactPhone', 'Некорректный формат телефона'),
			...emailField('contactEmail', 'Некорректный формат почты'),
			clientName: {
				...requiredField('clientName', 'Имя клиента обязательно').clientName,
				...minLengthField('clientName', 'Минимум 4 символа', 4).clientName
			},
		}
	);

	const isLoading = ref(false);

	const emit = defineEmits(['close']);

	const createClient = async () =>
	{
		const { valid } = await r$.$validate();

		if (!valid)
			return;

		isLoading.value = false;

		try {
			const response = await clients.createClient(newClient.value);

			if (response.client_id)
			{
				addToast('Клиент добавлен', 'success');
				addClient(response);
				emit('close');
			}
		}
		catch (err) { useRequestError(err); }
		finally { isLoading.value = false; }
	}
</script>

<template>
	<div class="client-wrapper">
		<p>Новый клиент</p>
		<div class="body">
			<div class="inputs">
				<UiInput
					variant="small"
					v-model="newClient.clientName"
					placeholder="Имя клиента"
					:error="r$.$errors.clientName[0]"
				/>
				<UiInput
					variant="small"
					v-model="newClient.fullName"
					placeholder="Полное имя клиента"
				/>
				<UiInput
					variant="small"
					v-model="newClient.inn"
					placeholder="ИНН"
					:onlyNumbers="true"
					:maxLength="12"
				/>
				<UiInput
					variant="small"
					v-model="newClient.addressLegal"
					placeholder="Адрес регистрации"
				/>
				<UiInput
					variant="small"
					v-model="newClient.addressActual"
					placeholder="Фактический адрес"
				/>
				<UiInput
					variant="small"
					v-model="newClient.contactPerson"
					placeholder="Контактное лицо"
				/>
				<UiInput
					variant="small"
					v-model="newClient.contactPhone"
					placeholder="Телефон"
					mask="+7(###)###-##-##"
					:error="r$.$errors.contactPhone[0]"
				/>
				<UiInput
					variant="small"
					v-model="newClient.contactEmail"
					placeholder="Email"
					:error="r$.$errors.contactEmail[0]"
				/>

			</div>
			<div class="buttons">
				<UiButton
					variant="green"
					:disabled="isLoading"
					@click="createClient"
				>
					Добавить
				</UiButton>
				<UiButton
					variant="dark"
					@click="emit('close')"
				>
					Отменить
				</UiButton>
			</div>
		</div>
	</div>
</template>

<style scoped lang='scss'>
	.client-wrapper
	{
		row-gap: 10px;

		display: flex;
		flex-direction: column;
	}

	.inputs
	{
		gap: 20px;
		margin-bottom: 20px;

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