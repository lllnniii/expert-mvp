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
				validator: (v) => ['dark', 'green'].includes(v)
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
		<slot />
	</component>
</template>

<style scoped lang='scss'>
	.button
	{
		width: max-content;
		padding: 14px 20px;
		line-height: 19px;
		font-weight: 600;
		border-radius: 10px;

		@include tr(.3, opacity, box-shadow);

		&:disabled
		{
			pointer-events: none;
			opacity: 0.3;
		}

		&--green
		{
			color: $primary;
			background-color: $green;

			&:hover { opacity: 0.8; }
		}

		&--dark
		{
			color: $white;
			background-color: $primary;
			box-shadow: inset 0 0 1px 0.5px $dark;

			&:hover
			{
				box-shadow: inset 0 0 3px 2px $dark;
			}
		}
	}
</style>