<script setup>
	const userStore = useUserStore();

	definePageMeta({ layout: 'unauth' });
	useSeoMeta({ title: 'Регистрация' });

	const form = ref(
		{
			username  : '',
			password  : ''
		}
	);

	const isLoading = ref(false);

	const {
		requiredField,
		passwordField
	} = useValidation();

	const { r$ } = useRegle(form.value,
		{
			...requiredField('username', 'Логин обязателен'),
			...passwordField()
		}
	);

	const registration = async () =>
	{

		const { valid } = await r$.$validate();

		if (!valid)
			return;

		isLoading.value = true;

		try {
			const response = await userStore.registration(form.value);

			if (!response?.detail)
				navigateTo('/login');
		}
		catch (err) { useRequestError(err) }
		finally { isLoading.value = false; }
	}
</script>

<template>
	<div class="wrapper">
		<form class="form">
			<div class="title">Регистрация</div>
			<UiInput
				type="text"
				:error="r$.$errors.username[0]"
				placeholder="Введите логин"
				v-model="form.username"
			/>
			<UiInput
				type="password"
				:error="r$.$errors.password[0]"
				placeholder="Введите пароль"
				v-model="form.password"
				@keyup.enter="registration"
			/>
			<div class="buttons">
				<UiButton
					@click="registration"
					:disabled="isLoading"
				>
					Регистрация
				</UiButton>
				<UiButton to="/login" variant="dark">Вход</UiButton>
			</div>
		</form>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		flex-grow: 1;

		display: flex;
		align-items: center;
		justify-content: center;
	}

	.title
	{
		color: $green;
		font-size: 24px;
		text-align: center;
		font-weight: 500;
	}

	.form
	{
		row-gap: 20px;

		display: flex;
		align-items: center;
		flex-direction: column;

		.input-wr { width: 100%; }
	}

	.buttons
	{
		column-gap: 10px;

		display: flex;
	}
</style>