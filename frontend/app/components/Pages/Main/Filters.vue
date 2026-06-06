<script setup>
	defineProps(
		{
			items:
			{
				type     : Array,
				required : true
			},
			activeFilterId:
			{
				type     : Number,
				required : true
			}
		}
	);

	const model = defineModel();

	const emit = defineEmits(['changeActiveFilter']);
</script>

<template>
	<div class="wrapper">
		<UiInput
			class="input"
			v-model="model"
			placeholder="Поиск объекта по названию"
		>
			<IconsMagnifier />
		</UiInput>
		<div class="filters">
			<button
				v-for="filter in items"
				:key="filter.id"
				class="filter"
				:class="{ 'active': filter.id === activeFilterId }"
				@click="emit('changeActiveFilter', filter.id)"
			>
				<span class="text">{{ filter.text }}</span>
				<span class="count">{{ filter.count }}</span>
			</button>
		</div>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		column-gap: 14px;

		display: flex;
	}

	.input { width: 100%; }

	.filters
	{
		border: 1px solid $light-gray;
		padding: 4px;
		column-gap: 6px;
		border-radius: 10px;
		background-color: $dark-gray;

		display: flex;
		flex-grow: 1;
		flex-shrink: 0;
	}

	.filter
	{
		color: $gray;
		cursor: pointer;
		padding: 9px 14px;
		column-gap: 6px;
		flex-shrink: 0;
		border-radius: 7px;

		display: flex;

		@include tr(.3, background-color, box-shadow);

		.text
		{
			color: $gray;

			@include tr(.3, color);
		}

		.count
		{
			color: $light-gray-text;
			@include tr(.3, color);
		}

		&.active
		{
			box-shadow: inset 0 0 0 1px $light-gray;
			background-color: $primary;

			.text { color: $green; }
			.count { color: $gray; }
		}
	}
</style>