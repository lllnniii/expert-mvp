<script setup>
	const toastsStore = useToastsStore();
</script>

<template>
	<div class="wrapper">
		<div class="content">
			<div class="text">
				<h1 class="title">Управление<br><span class="highlighted">объектами</span> предприятия</h1>
				<p class="subtitle">Реестр опасных производственных объектов: учёт по классам ОПО, привязка к клиентам, экспертиза промышленной безопасности и сопровождение проектов.</p>
			</div>
			<div class="buttons">
				<UiButton
					variant="dark"
					@click="toastsStore.addToast('Пока не работает', 'info')"
				>
					<template #icon><IconsExport /></template>
					Экспорт
				</UiButton>
				<UiButton
					variant="green"
				>
					<template #icon><IconsPlus/></template>
					Добавить объект
				</UiButton>
			</div>
		</div>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		padding-bottom: 32px;
		border-bottom: 1px solid $light-gray;
	}

	.content
	{
		padding: 0 40px;

		display: flex;
		justify-content: space-between;
	}

	.title
	{
		font-size: 48px;
		font-weight: 700;
		line-height: 50.4px;
		margin-bottom: 15px;
		letter-spacing: -1.44px;
	}

	.highlighted { color: $green; }

	.subtitle
	{
		color: $gray;
		font-size: 15px;
		max-width: 490px;
		line-height: 24px;
	}

	.buttons
	{
		column-gap: 10px;

		display: flex;
		align-self: flex-end;
	}
</style>