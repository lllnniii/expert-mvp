<script setup>
	const filters = ref(
		[
			{
				id    : 0,
				text  : 'Все',
				count : '0',
			},
			{
				id    : 1,
				text  : 'I класс',
				count : '0',
			},
			{
				id    : 2,
				text  : 'II класс',
				count : '0'
			},
			{
				id    : 3,
				text  : 'III класс',
				count : '0'
			},
			{
				id    : 4,
				text  : 'IV класс',
				count : '0'
			}
		]
	);

	const activeFilterId = ref(filters.value[0].id);
	const searchString   = ref('');

	const changeActiveFilter = (filterId) => activeFilterId.value = filterId;
</script>

<template>
	<PagesMainHead />
	<div class="page-content">
		<PagesMainFilters
			:items="filters"
			:activeFilterId
			v-model="searchString"
			@changeActiveFilter="changeActiveFilter"
		/>
	</div>
</template>

<style scoped lang='scss'>
	.page-content { padding: 40px; }
</style>