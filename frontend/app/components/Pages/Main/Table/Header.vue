<script setup>
	defineProps(
		{
			count:
			{
				type     : Number,
				required : true
			}
		}
	);
</script>

<template>
	<div class="wrapper">
		<p class="title">Реестр объектов</p>
		<p class="counter">
			Показано
			<span class="count">{{ count }}</span>
			объектов
		</p>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		padding: 18px 22px;
		border: 1px solid $light-gray;
		border-radius: 14px 14px 0 0;
		border-bottom: none;
		background-color: $dark-gray;

		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.title
	{
		font-size: 15px;
		font-weight: 700;
		letter-spacing: -0.15px;
	}

	.counter { color: $gray; }

	.count { color: $white; }
</style>