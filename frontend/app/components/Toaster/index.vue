<script setup>
	const toastsStore = useToastsStore();
</script>

<template>
	<div class="wrapper">
		<TransitionGroup name="toast">
			<ToasterItem
				v-for="toast in toastsStore.toasts"
				:key="toast.id"
				:id="toast.id"
				:variant="toast.variant"
			>
				{{ toast.text }}
			</ToasterItem>
		</TransitionGroup>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		z-index: 2;
		transform: translateX(50%);

		top: 30px;
		right: 50%;
		display: flex;
		position: fixed;
		align-items: center;
		flex-direction: column;
	}
</style>