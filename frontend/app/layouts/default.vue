<script setup>
	const nuxtApp   = useNuxtApp();
	const userStore = useUserStore();

	useSeoMeta({ title: 'PromExpert' });

	const isLoading = ref(false);

	nuxtApp.hook("page:start", () => isLoading.value = true);
	nuxtApp.hook("page:finish", () =>
		{
			getScrollWidth();
			isLoading.value = false;
		}
	);

	if (!userStore.user?.id)
	{
		try { await userStore.getCurrentUser(); }
		catch (err)
		{
			const refreshToken = useCookie("promTokenRefresh");

			if (refreshToken.value)
			{
				try
				{
					const response = await userStore.refresh(refreshToken.value);

					if (response.refresh_token)
						refreshToken.value = response.refresh_token;
				}
				catch (err)
				{
					console.error(err)
					navigateTo('/login')
				}
			}
			else
				navigateTo('/login');
		}
	}
</script>

<template>
	<div class="default-layout">
		<Header />
		<main class="container">
			<Transition name="fade" mode="out-in">
				<NuxtPage />
			</Transition>
		</main>
	</div>

	<Loader v-if="isLoading" />

	<Teleport to="body">
		<Toaster />
	</Teleport>

	<PopupContainer />
</template>

<style lang='scss'>
	.default-layout
	{
		min-height: 100vh;
		background-color: $primary;

		display: flex;
		flex-direction: column;

		main
		{
			flex-grow: 1;

			display: flex;
			flex-direction: column;
		}
	}
</style>