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
		await userStore.getCurrentUser();
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