<script setup>
	defineProps(
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
		@click="toggleMenu(!isOpened)"
	>
		<template #icon>
			<IconsBurger />
		</template>
		Меню
	</UiButton>

	<Transition name="fade-left">
		<HeaderMenu
			v-if="isOpened"
			@toggleMenu="toggleMenu"
		/>
	</Transition>
</template>