<script setup>
	const isMenuOpened = ref(false);

	const toggleMenu = (value) => isMenuOpened.value = value;
</script>

<template>
	<header class="wrapper">
		<div class="content">
			<HeaderLogo />
			<HeaderMenuButton
				:isOpened="isMenuOpened"
				@toggleMenu="toggleMenu"
			/>
		</div>
	</header>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		border-bottom: 1px solid $light-gray;

		display: flex;
		align-items: center;
		flex-direction: column;
	}

	.content
	{
		width: 100%;
		padding: 18px 40px;
		max-width: 1440px;
		background-color: rgba($primary, 0.85);

		display: flex;
		align-items: center;
		justify-content: space-between;
	}
</style>