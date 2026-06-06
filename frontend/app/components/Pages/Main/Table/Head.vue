<script setup></script>

<template>
	<thead class="head">
		<tr>
			<td>ID</td>
			<td>Наименование</td>
			<td>Адрес</td>
			<td>Клиент</td>
			<td>Категория ОПО</td>
			<td>Действия</td>
		</tr>
	</thead>
</template>

<style scoped lang='scss'>
	.head
	{
		width: 100%;
		border: 1px solid $light-gray;
		background-color: rgba($white, 0.015);

		td
		{
			color: $gray;
			padding: 14px 22px;
			font-size: 11px;
			font-weight: 600;
			letter-spacing: 1.54px;
			text-transform: uppercase;

			&:last-child { text-align: right; }
		}
	}
</style>