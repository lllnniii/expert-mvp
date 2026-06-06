<script setup>
	const { objects: objectsApi } = useApi();
	const { addToast }            = useToastsStore();
	const objectsStore            = useObjectsStore();
	const popupsStore             = usePopupsStore();

	const props = defineProps(
		{
			id:
			{
				type     : Number,
				required : true
			},
			name:
			{
				type     : String,
				required : true
			},
			address:
			{
				type     : String,
				required : true
			},
			clientName:
			{
				type     : String,
				required : true
			},
			oposCategory:
			{
				type     : String,
				required : true
			},
			description:
			{
				type     : String,
				required : true
			 }
		}
	);

	const isLoading  = ref(false);
	const isExpanded = ref(false);

	const deleteObject = async () =>
	{
		isLoading.value = true;

		try
		{
			const response = await objectsApi.deleteObject(props.id);

			if (!response?.detail)
			{
				await objectsStore.getObjects();
				addToast('Объект удален', 'success');
			}
		}
		catch (err) { useRequestError(err); }
		finally { isLoading.value = false; }
	};

	const openEditObjectPopup = () =>
	{
		popupsStore.togglePopup('editObject', true);
		popupsStore.setPopupData(
			{
				id           : props.id,
				name         : props.name,
				address      : props.address,
				description  : props.description,
				oposCategory : props.oposCategory
			}
		);
	};

	const toggleExpand = () => isExpanded.value = !isExpanded.value;
</script>

<template>
	<tr
		class="item"
		:class="{ 'disabled': isLoading }"
	>
		<td class="id">{{ id }}</td>
		<td class="name">{{ name }}</td>
		<td class="address">{{ address }}</td>
		<td class="client">
			<span
				v-if="getClientAbbr(clientName)"
				class="client-abbreviature"
			>
				{{ getClientAbbr(clientName) }}
			</span>
			<span class="client-name">
				{{ clientName }}
			</span>
		</td>
		<td
			class="opos"
			:class="getOposCategoryClassName(oposCategory)"
		>
			<span
				v-if="oposCategory"
				class="info"
			>
				<span class="indicator" />
				<span class="text">
					{{ oposCategory }} ОПО
				</span>
			</span>
		</td>

		<td class="buttons">
			<UiButton
				variant="dark"
				@click="toggleExpand"
			>
				<template #icon>
					<IconsEye />
				</template>
			</UiButton>

			<UiButton
				variant="dark"
				@click="openEditObjectPopup"
			>
				<template #icon>
					<IconsEdit />
				</template>
			</UiButton>

			<UiButton
				variant="dark"
				@click="deleteObject"
			>
				<template #icon>
					<IconsTrash />
				</template>
			</UiButton>
		</td>
	</tr>

	<Transition name="fade">
		<tr v-if="isExpanded" class="expanded-row">
			<td colspan="6" class="description-cell">
				<div class="description-content">
					<span class="label">Описание объекта:</span>
					<p class="text">{{ description || 'Описание отсутствует' }}</p>
				</div>
			</td>
		</tr>
	</Transition>
</template>

<style scoped lang='scss'>
	.item
	{
		background-color: $dark-gray;

		@include tr(.3, opacity, background-color);

		&:hover { background-color: lighten($dark-gray, $amount: 1); }

		&.disabled
		{
			opacity: 0.5;
			pointer-events: none;
		}
	}

	.item td
	{
		padding: 22px 18px;
		font-size: 13px;

		&:first-child,
		&:last-child { padding: 0 18px; }
	}

	.expanded-row
	{
		background-color: darken($dark-gray, 2%);

		.description-cell
		{
			padding: 0 18px 24px 18px;

			.description-content
			{
				background-color: rgba($white, 0.03);
				border-left: 3px solid $green;
				border-radius: 0 8px 8px 0;
				padding: 16px 20px;

				.label
				{
					color: $light-gray-text;
					font-size: 11px;
					font-weight: 700;
					margin-bottom: 8px;
					text-transform: uppercase;
					letter-spacing: 0.5px;

					display: block;
				}

				.text
				{
					color: $white;
					margin: 0;
					font-size: 13px;
					word-break: break-word;
					line-height: 1.6;
					white-space: pre-wrap;
				}
			}
		}
	}

	.id
	{
		color: $light-gray-text;
		width: 117px;
	}

	.name
	{
		color: $white;
		width: 406px;
	}

	.address
	{
		width: 259px;
		color: $gray;
		letter-spacing: -0.13px;
	}

	.client
	{
		width: 244px;
		column-gap: 10px;

		display: flex;
		align-items: center;

		&-name
		{
			color: $white;
			font-size: 14px;
		}

		&-abbreviature
		{
			color: $white;
			padding: 6px;
			font-size: 11px;
			font-weight: 700;
			border-radius: 100%;
			background-color: $light-gray;
		}
	}

	.opos
	{
		width: 168px;
		font-size: 12px;
		font-weight: 600;

		.info
		{
			width: max-content;
			border: 1px solid $light-gray;
			padding: 5px 10px;
			column-gap: 8px;
			border-radius: 100px;
			background-color: $primary;

			display: flex;
			align-items: center;
		}

		.indicator
		{
			width: 6px;
			height: 6px;
			border-radius: 100px;
		}

		&.violet
		{
			.indicator { background-color: $violet; }
			.text { color: $violet; }
		}

		&.red
		{
			.indicator { background-color: $red; }
			.text { color: $red; }
		}

		&.yellow
		{
			.indicator { background-color: $yellow; }
			.text { color: $yellow; }
		}

		&.green
		{
			.indicator { background-color: $green; }
			.text { color: $green; }
		}
	}

	.buttons
	{
		width: 161px;
		column-gap: 6px;

		display: flex;
		justify-content: flex-end;

		button
		{
			padding: 8px;
			color: $gray;
		}
	}
</style>