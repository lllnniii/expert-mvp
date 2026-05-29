<script setup>
	const userStore = useUserStore();

	const userName = userStore.user?.name[0];

	const isLoading = ref(false);

	const logout = async () =>
	{
		isLoading.value = true;

		try
		{
			const refreshToken = useCookie('promTokenRefresh');
			const accessToken  = useCookie('promTokenAccess');

			await userStore.logout(refreshToken.value);

			accessToken.value  = '';
			refreshToken.value = '';

			userStore.setUserData(null);

			navigateTo('/login');
		}
		catch (err) { console.error(err) }
		finally { isLoading.value = false; }
	}
</script>

<template>
	<div class="user">
		<div class="info">
			<div class="avatar">{{ userName }}</div>
			<div class="name">{{ userStore.user?.name }}</div>
		</div>
		<UiButton
			variant="gray"
			class="logout"
			:disabled="isLoading"
			@click="logout"
		>
			<IconsLogout />
		</UiButton>
	</div>
</template>

<style scoped lang='scss'>
	.user
	{
		padding: 24px 26px;
		border-bottom: 1px solid $light-gray;

		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.info
	{
		column-gap: 14px;

		display: flex;
		align-items: center;
	}

	.avatar
	{
		width: 46px;
		height: 46px;
		color: $green;
		border: 1px solid $light-gray;
		font-size: 15px;
		font-weight: 700;
		border-radius: 12px;
		text-transform: uppercase;
		background-color: rgba($green, 0.08);

		display: flex;
		align-items: center;
		justify-content: center;
	}

	.name
	{
		font-size: 16px;
		font-weight: 600;
		letter-spacing: -0.16px;
		text-transform: capitalize;
	}

	.logout
	{
		color: $red;
		padding: 13px;
		background-color: rgba($red, 0.08);
	}
</style>