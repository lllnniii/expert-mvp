<script setup>
	const props = defineProps(
		{
			disabled:
			{
				type: Boolean,
				required: false,
				default: false
			},
			to:
			{
				type     : String,
				required : false,
				default  : ''
			},
			variant:
			{
				type: String,
				required: false,
				default: 'green',
				validator: (v) => ['dark', 'gray', 'green'].includes(v)
			}
		}
	);

	const tag = computed(() => props.to ? resolveComponent('NuxtLink') : 'button');
</script>

<template>
	<component
		class="button"
		:class="`button--${variant}`"
		:is="tag"
		type="button"
		:disabled
		:to
	>
		<span class="icon">
			<slot name="icon" />
		</span>
		<slot />
	</component>
</template>

<style scoped lang='scss'>
	.button
	{
		width: max-content;
		padding: 14px 20px;
		column-gap: 10px;
		line-height: 19px;
		font-weight: 600;
		border-radius: 10px;

		display: flex;
		align-items: center;

		@include tr(.3, opacity, box-shadow, background-color, transform);

		&:active { transform: translateY(2px) scale(0.98); }

		&:disabled
		{
			opacity: 0.3;
			pointer-events: none;
		}

		&:has(svg)
		{
			.icon { display: flex; }
		}

		&--green
		{
			color: $primary;
			background-color: $green;

			&:hover { opacity: 0.8; }
		}

		&--gray
		{
			color: $white;
			box-shadow: inset 0 0 0 1px $light-gray;
			background-color: $dark-gray;

			&:hover
			{
				box-shadow: inset 0 0 0 1px darken($dark-gray, 1);
				background-color: darken($dark-gray, 1);
			}
		}

		&--dark
		{
			color: $white;
			background-color: $primary;
			box-shadow: inset 0 0 0 1px $dark;

			&:hover
			{
				box-shadow: inset 0 0 0 2px $dark;
			}
		}

		.icon
		{
			width: 14px;
			height: 14px;

			display: none;
			flex-shrink: 0;
			align-items: center;
			justify-content: center;
		}
	}
</style>