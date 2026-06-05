<script setup>
	const props = defineProps(
		{
			items:
			{
				type     : Array,
				required : true
			},
			currentItemId:
			{
				type     : Object,
				required : true
			},
			placeholder:
			{
				type     : String,
				required : false
			},
			textFieldName:
			{
				type     : String,
				required : true
			},
			error:
			{
				type: String,
				required: true
			}
		}
	);

	const isOpened = ref(false);
	const search   = ref('');

	const emit = defineEmits(['chooseSelectItem']);

	const currentItem    = computed(() => props.items.find(item => item.id === props.currentItemId));

	const displayedItems = computed(() =>
		{
			if (!search.value)
				return props.items.filter(item => item.id !== props.currentItemId)

			return props.items.filter(item => item[props.textFieldName].toLowerCase().includes(search.value.trim().toLowerCase()))
		}
);

	const toggleContent = () =>
	{
		isOpened.value = !isOpened.value;

		if (!isOpened.value)
			search.value = '';
	};

	const chooseItem = (item) =>
	{
		emit('chooseSelectItem', item.id);
		isOpened.value = false;
		search.value   = '';
	};
</script>

<template>
	<div class="select-wrapper">
		<div class="head" @click="toggleContent">
			<div v-if="!isOpened" class="current">
				<span v-if="currentItem">{{ currentItem[textFieldName] }}</span>
				<span v-else class="current--placeholder">{{ placeholder }}</span>
			</div>

			<div v-else class="current search-wrapper">
				<input
					type="search"
					placeholder="Поиск"
					v-model.trim="search"
					@click.stop
				>
			</div>
			<IconsArrow class="icon" :class="{ 'active': isOpened }" />
		</div>

		<Transition name="fade">
			<span class="error">{{ error }}</span>
		</Transition>

		<Transition name="fade">
			<div
				v-if="isOpened"
				class="content"
			>
				<div
					v-for="item in displayedItems"
					:key="item.id"
					class="item"
					@click="chooseItem(item)"
				>
					{{ item[textFieldName] }}
				</div>
			</div>
		</Transition>

	</div>
</template>

<style scoped lang='scss'>
	.select-wrapper { position: relative; }

	.head
	{
		cursor: pointer;
		padding: 10px 15px;
		box-shadow: inset 0 0 1px 1px $light-gray;
		line-height: 19px;
		border-radius: 10px;
		background-color: $dark-gray;

		display: flex;
		justify-content: space-between;
		align-items: center;

	}

	.current
	{
		color: $white;

		&--placeholder { color: $light-gray-text; }
	}

	.search-wrapper
	{
		max-width: 80%;
	}

	.icon
	{
		color: $light-gray-text;
		transform: rotate(180deg);

		@include tr(.3, transform);

		&.active { transform: rotate(0); }
	}

	.error
	{
		color: $red;
		font-size: 12px;
	}

	.content
	{
		width: 100%;
		row-gap: 5px;
		padding: 10px;
		max-height: 150px;
		overflow-y: scroll;
		scrollbar-width: thin;
		border-radius: 10px;
		background-color: $dark-gray;

		top: calc(100% + 10px);
		display: flex;
		position: absolute;
		flex-direction: column;
	}

	.item
	{
		cursor: pointer;
		border-radius: 10px;
		padding: 5px 10px;

		@include tr(.3, background-color);

		&:hover { background-color: rgba($white, 0.1); }
	}
</style>