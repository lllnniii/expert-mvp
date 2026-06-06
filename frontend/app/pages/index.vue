<script setup>
	const objectsStore = useObjectsStore();

	const filters = computed(() =>
	{
		const objects = objectsStore.objects;

		const uniqueCategories = [...new Set(objects.map(obj => obj.oposCategory).filter(Boolean))];

		uniqueCategories.sort((a, b) => a.localeCompare(b, 'ru'));

		const result =
		[
			{
				id: 0,
				text: 'Все',
				count: objects.length,
			}
		];

		uniqueCategories.forEach((category, index) =>
		{
			result.push(
				{
					id: index + 1,
					text: category,
					count: objects.filter(object => object.oposCategory === category).length
				}
			);
		});

		return result;
	});

	const activeFilterId = ref(0);
	const searchString = ref('');

	const changeActiveFilter = (filterId) => activeFilterId.value = filterId;

	const displayedObjects = computed(() =>
	{
		let result = objectsStore.objects;

		if (activeFilterId.value !== 0)
		{
			const activeFilter = filters.value.find(f => f.id === activeFilterId.value);

			if (activeFilter)
				result = result.filter(object => object.oposCategory === activeFilter.text);
		}

		if (searchString.value)
		{
			const search = searchString.value.trim().toLowerCase();
			result       = result.filter(object => object.name.trim().toLowerCase().includes(search));
		}

		return result;
	});

	await objectsStore.getObjects();
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

	<PagesMainTable
	  :items="displayedObjects"
	/>
  </div>
</template>

<style scoped lang='scss'>
	.page-content
	{
		row-gap: 20px;
		padding: 40px;

		display: flex;
		flex-direction: column;
	}
</style>