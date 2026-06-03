<script setup>
	const nuxtApp   = useNuxtApp();
	const userStore = useUserStore();

	useSeoMeta({ title: 'PromExpert' });

	nuxtApp.hook("page:finish", () => getScrollWidth());

	if (!userStore.user?.id)
		await userStore.getCurrentUser();
</script>

<template>
	<div class="default-layout">
		<Header />
		<main>
			<Transition name="fade" mode="out-in">
				<NuxtPage />
			</Transition>
		</main>
	</div>

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