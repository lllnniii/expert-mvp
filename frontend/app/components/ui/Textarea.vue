<script setup>
	defineProps(
		{
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
	<textarea
		class="textarea"
		:placeholder
		:value="model"
		@input="inputHandler"
	/>
</template>

<style scoped lang='scss'>
	.textarea
	{
		resize: none;
		padding: 10px;
		min-height: 150px;
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

		&:focus { box-shadow: inset 0 0 0 1px $green; }
	}
</style>