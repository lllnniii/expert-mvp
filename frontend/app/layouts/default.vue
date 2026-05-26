<script setup>
	const nuxtApp = useNuxtApp();

	useSeoMeta({ title: 'PromExpert' });

	nuxtApp.hook("page:finish", () => getScrollWidth());
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
</template>

<style lang='scss'>
	.default-layout
	{
		min-height: 100vh;
		background-color: $primary;

		display: flex;
		flex-direction: column;

		main { flex-grow: 1; }
	}
</style>