<script setup>
	defineProps(
		{
			label:
			{
				type     : String,
				required : false,
				default  : ''
			},
			type:
			{
				type     : String,
				required : false,
				default  : false
			},
			placeholder:
			{
				type     : String,
				required : true,
			},
			error:
			{
				type     : String,
				required : false
			}
		}
	);

	const model = defineModel();

	const inputHandler = (e) =>
	{
		const inputValue = e.target.value;
		model.value = inputValue;
	}
</script>

<template>
	<div class="input-wr">
		<div
			v-if="label"
			class="label"
		>
			{{ label }}
		</div>
		<input
			class="input"
			:type
			:placeholder
			:value="model"
			@input="inputHandler"
		/>
		<Transition name="fade">
			<span
				v-if="error"
				class="error"
			>
				{{ error }}
			</span>
		</Transition>
	</div>
</template>

<style scoped lang='scss'>
	.input-wr
	{
		row-gap: 5px;

		display: flex;
		flex-direction: column;
	}

	.label
	{
		color: $gray;
		font-weight: 500;
	}

	.input
	{
		padding: 10px 15px;
		box-shadow: inset 0 0 1px 1px $light-gray;
		line-height: 19px;
		border-radius: 10px;
		background-color: $dark-gray;

		@include tr(.3, box-shadow);

		&::placeholder
		{
			color: $light-gray-text;
			line-height: 19px;
		}

		&:focus { box-shadow: inset 0 0 1px 1px $green; }
	}

	.error
	{
		color: $red;
		font-size: 12px;
	}
</style>