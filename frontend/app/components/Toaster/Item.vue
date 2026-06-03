<script setup>
	const props = defineProps(
		{
			variant:
			{
				type      : String,
				required  : false,
				default   : 'info',
				validator : (v) => ['success', 'info', 'error'].includes(v)
			},
			id:
			{
				type     : Number,
				required : true
			}
		}
	);

	const toastsStore = useToastsStore();

	const removeToast = () => toastsStore.removeToast(props.id);
</script>

<template>
	<div
		class="item"
		:class="`item--${variant}`"
		@click="removeToast"
	>
		<slot />
	</div>
</template>

<style scoped lang='scss'>
	.item
	{
		color: $white;
		cursor: pointer;
		padding: 5px 10px;
		overflow: hidden;
		font-weight: 500;
		user-select: none;
		border-radius: 5px;
		margin-bottom: 10px;

		@include tr(.3, opacity, transform, box-shadow);

		&:last-child { margin-bottom: 0; }

		&:hover
		{
			opacity: 0.7;
			transform: translateY(2px);
			box-shadow: none;
		}

		&:active { transform: translateY(2px) scale(0.95); }

		&--success
		{
			background-color: $green;
			box-shadow: 0 0 3px 3px rgba($green, 0.3);
		}

		&--info
		{
			background-color: $yellow;
			color: $primary;
			box-shadow: 0 0 3px 3px rgba($yellow, 0.3);
		}

		&--error
		{
			background-color: $red;
			box-shadow: 0 0 3px 3px rgba($red, 0.3);
		}
	}
</style>