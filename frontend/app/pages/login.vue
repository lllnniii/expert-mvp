<script setup>
	const userStore = useUserStore();

	const form = ref(
		{
			username: '',
			password: ''
		}
	);
	const isLoading = ref(false);

	const login = async () =>
	{
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
			}
		}
		catch (err) { console.error(err) }
		finally { isLoading.value = false; }
	}
</script>

<template>
	<div class="wrapper">
		<form class="form">
			<input
				type="text"
				placeholder="Логин"
				v-model="form.username"
			>
			<input
				type="password"
				placeholder="Пароль"
				v-model="form.password"
			>
			<button
				type="button"
				@click="login"
			>
				Войти
			</button>
		</form>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		width: 100%;
		height: 100%;

		display: flex;
		align-items: center;
		justify-content: center;
	}

	.form
	{

	}
</style>