<script setup>
	const userStore = useUserStore();

	const form = ref(
		{
			username  : '',
			password  : ''
		}
	);

	const isLoading = ref(false);

	const registration = async () =>
	{
		isLoading.value = true;

		try {
			const response = await userStore.registration(form.value);

			if (!response?.detail)
				navigateTo('/login');
		}
		catch (err) { console.error(err.data.detail) }
		finally { isLoading.value = false; }
	}
</script>

<template>
	<div class="wrapper">
		<div class="form">
			<input
				type="text"
				name=""
				placeholder="Имя пользователя"
				v-model="form.username"
			>
			<input
				type="password"
				name=""
				placeholder="Пароль"
				v-model="form.password"
			>
			<button
				type="button"
				class="button"
				@click="registration"
			>
				Рега
			</button>
		</div>
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
</style>