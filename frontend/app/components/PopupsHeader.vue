<script setup>
	const { closeCurrentPopup } = usePopupsStore();

	defineProps(
		{
			title:
			{
				type     : String,
				required : true
			}
		}
	);
</script>

<template>
	<div class="header">
		<p class="title">{{ title }}</p>
		<IconsClose class="close" @click="closeCurrentPopup" />
	</div>
</template>

<style scoped lang='scss'>
	.header
	{
		column-gap: 20px;
		margin-bottom: 30px;

		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.title
	{
		font-size: 24px;
		line-height: 100%;
		font-weight: 500;
	}

	.close
	{
		width: 16px;
		height: 16px;
		cursor: pointer;
		color: rgba($red, 0.3);

		@include tr(0.3, color);

		&:hover { color: $red; }
	}
</style>