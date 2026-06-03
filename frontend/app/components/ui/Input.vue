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
				default  : 'text'
			},
			variant:
			{
				type      : String,
				required  : false,
				default   : 'normal',
				validator : (v) => ['small', 'normal'].includes(v)
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
			:class="`input--${variant}`"
			:type
			:placeholder
			:value="model"
			@input="inputHandler"
		/>
		<span v-if="$slots.default" class="icon">
			<slot />
		</span>
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
		position: relative;
		flex-direction: column;

		&:has(svg)
		{
			.input { padding-left: 45px; }

			.icon
			{
				color: $gray;
				width: 18px;
				height: 18px;
				transform: translateY(-50%);

				top: 50%;
				left: 16px;
				display: flex;
				position: absolute;
				align-items: center;
				justify-content: center;
			}

			&:has(.error) .icon { top: 19px; }
		}
	}

	.label
	{
		color: $gray;
		font-weight: 500;
	}

	.input
	{
		box-shadow: inset 0 0 1px 1px $light-gray;
		line-height: 19px;
		border-radius: 10px;
		background-color: $dark-gray;

		@include tr(.3, box-shadow);

		&--normal { padding: 16px; }

		&--small { padding: 10px 15px; }

		&::placeholder
		{
			color: $light-gray-text;
			line-height: 19px;
		}

		&:focus { box-shadow: inset 0 0 0 1px $green; }
	}

	.error
	{
		color: $red;
		font-size: 12px;
	}
</style>