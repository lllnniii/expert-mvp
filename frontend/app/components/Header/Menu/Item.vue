<script setup>
	defineProps(
		{
			title:
			{
				type     : String,
				required : true
			},
			link:
			{
				type     : String,
				required : true
			},
			icon:
			{
				type     : Object,
				required : true
			},
			count:
			{
				type     : Number,
				required : true
			}
		}
	);
</script>

<template>
	<li class="item-wrapper">
		<NuxtLink
			:to="link"
			class="item"
		>
			<div class="label">
				<span class="icon-wrapper">
					<component :is="icon" />
				</span>
				<span class="text">{{ title }}</span>
			</div>
			<div class="counter">
				{{ count }}
			</div>
		</NuxtLink>
	</li>
</template>

<style scoped lang='scss'>
	.item
	{
		padding: 12px 13px;
		border-radius: 10px;

		display: flex;
		position: relative;
		justify-content: space-between;

		@include tr(.3, background-color);

		&:hover,
		&.router-link-active
		{
			background-color: rgba($green, 0.08);

			.icon-wrapper { color: $green; }
			.text { color: $green; }
			.counter
			{
				color: $primary;
				background-color: $green;
				border-color: $green;
			}
		}

		&.router-link-active
		{
			&::before
			{
				width: 3px;
				height: 22px;
				content: '';
				transform: translateY(-50%);
				border-radius: 2px;
				background-color: $green;

				left: calc(0% - 15px);
				top: 50%;
				position: absolute;

				@include tr(.3, height);
			}
		}
	}

	.label
	{
		column-gap: 14px;

		display: flex;
		align-items: center;
	}

	.icon-wrapper
	{
		color: $gray;
		height: 22px;
		width: 22px;

		display: flex;
		align-items: center;
		justify-content: center;

		@include tr(.3, color);
	}

	.text
	{
		color: $white;
		font-size: 15px;
		font-weight: 600;

		@include tr(.3, color);
	}

	.counter
	{
		color: $gray;
		padding: 2px 8px;
		font-size: 11px;
		font-weight: 500;
		border-radius: 6px;
		background-color: $primary;
		border: 1px solid $light-gray;

		@include tr(.3, color, background-color, border-color)
	}
</style>