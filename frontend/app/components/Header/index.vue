<script setup></script>

<template>
	<header class="wrapper">
		<div class="content">
			<HeaderLogo />
			
		</div>
	</header>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		display: flex;
		align-items: center;
		flex-direction: column;
	}

	.content
	{
		padding: 18px 40px;
		max-width: 1440px;
		background-color: rgba($primary, 0.85);

		display: flex;
		align-items: center;
		justify-content: space-between;
	}
</style>