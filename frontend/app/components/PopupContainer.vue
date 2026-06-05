<script setup>
	const popupsStore = usePopupsStore();

	const activeComponent = computed(() => usePopupsRegistry(popupsStore.activePopup));

	onKeyStroke('Escape', () =>
		{
			if (activeComponent.value)
				popupsStore.closeCurrentPopup();
		}
	);
</script>

<template>
	<Teleport to="#teleports">
		<Transition name="opacity">
			<div
				v-if="activeComponent"
				class="popup-wrapper"
			>
				<component :is="activeComponent" />
			</div>
		</Transition>
	</Teleport>
</template>

<style scoped lang='scss'>
	.popup-wrapper
	{
		z-index: 2;
		width: 100vw;
		height: 100dvh;
		padding-top: 0;
		padding-bottom: 0;
		backdrop-filter: blur(8px);
		background-color: rgba($primary, $alpha: 0.9);

		top: 50%;
		left: 50%;
		display: flex;
		position: fixed;
		align-items: center;
		justify-content: center;
		transform: translate(-50%, -50%);
	}
</style>