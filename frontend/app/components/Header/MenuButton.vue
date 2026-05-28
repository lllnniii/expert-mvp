<script setup>
	const props = defineProps(
		{
			isOpened:
			{
				type     : Boolean,
				required : true
			}
		}
	);

	const emit = defineEmits(['toggleMenu']);

	const toggleMenu = (value) => emit('toggleMenu', value);
</script>

<template>
	<UiButton
		variant="gray"
		@click="toggleMenu(!props.isOpened)"
	>
		<div class="menu-button">
			<div class="menu-icon">
				<span></span>
				<span></span>
				<span></span>
			</div>
			<span class="label">Меню</span>
		</div>
	</UiButton>

	<Transition name="fade-left">
		<HeaderMenu
			v-if="isOpened"
			@toggleMenu="toggleMenu"
		/>
	</Transition>
</template>

<style scoped lang='scss'>
	.menu-button
	{
		column-gap: 10px;

		display: flex;
		align-items: center;
	}

	.menu-icon
	{
		row-gap: 3px;

		display: flex;
		flex-direction: column;

		span
		{
			width: 16px;
			height: 2px;
			border-radius: 1px;
			background-color: $white;
		}
	}
</style>