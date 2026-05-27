<script setup>
	const userStore = useUserStore();

	const form = ref(
		{
			username: '',
			password: ''
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

	const login = async () =>
	{
		const { valid } = await r$.$validate();

		if (!valid)
			return;

		isLoading.value = true;

		const formData = new FormData();
		formData.append('username', form.value.username);
		formData.append('password', form.value.password);

		try {
			const response = await userStore.login(formData);

			if (response.access_token)
			{
				const accessToken = useCookie('promTokenAccess');

				accessToken.value = response.access_token;

				navigateTo('/');
			}
		}
		catch (err) { console.error(err) }
		finally { isLoading.value = false; }
	}
</script>

<template>
	<div class="wrapper">
		<form class="form">
			<div class="title">Вход</div>
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
				@keyup.enter="login"
			/>
			<div class="buttons">
				<UiButton
					@click="login"
					:disabled="isLoading"
				>
					Войти
				</UiButton>
				<UiButton to="/registration" variant="dark">Регистрация</UiButton>
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