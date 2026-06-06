<script setup>
	const props = defineProps(
		{
			items:
			{
				type     : Array,
				required : true
			}
		}
	);

	const itemsCount = computed(() => props.items.length);
</script>

<template>
	<div class="wrapper">
		<PagesMainTableHeader :count="itemsCount" />
		<table class="table">
			<PagesMainTableHead />
			<tbody>
				<TransitionGroup name="opacity">
					<PagesMainTableItem
						v-for="object in items"
						:key="object.id"
						:id="object.id"
						:name="object.name"
						:address="object.address"
						:clientName="object?.client?.name"
						:oposCategory="object.oposCategory"
					/>
				</TransitionGroup>
			</tbody>
		</table>
	</div>
</template>

<style scoped lang="scss">
	.table { width: 100%; }

	tbody
	{
		border: 1px solid $light-gray;
	}
</style>
