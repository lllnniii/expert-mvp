<script setup>
	const toastsStore = useToastsStore();

	toastsStore.addToast('Авторизация успешно провалена', 'info');
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
		transform: translateX(50%);

		top: 30px;
		right: 50%;
		display: flex;
		position: fixed;
		align-items: center;
		flex-direction: column;
	}
</style>