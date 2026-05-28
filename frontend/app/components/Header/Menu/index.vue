<script setup>
	import House from '~/components/icons/House.vue';

	const menuList =
	[
		{
			icon  : House,
			title : 'Объекты',
			count : 247,
			link  : '/'
		}
	]

	const emit = defineEmits(['toggleMenu']);

	onKeyStroke('Escape', () => emit('toggleMenu', false));
</script>

<template>
	<div class="wrapper">
		<div class="background" @click="emit('toggleMenu', false)" />
		<div class="content">
			<div class="header">
				<p class="title">Навигация</p>
				<UiButton
					variant="gray"
					class="close"
					@click="emit('toggleMenu', false)"
				>
					<IconsClose />
				</UiButton>
			</div>

			<div class="body">
				<div class="body-title-wrapper">
					<span class="body-title">Разделы</span>
				</div>
				<ul class="list">
					<HeaderMenuItem
						v-for="item in menuList"
						:key="`${item.link}-${item.title}`"
						:title="item.title"
						:link="item.link"
						:icon="item.icon"
						:count="item.count"
					/>
				</ul>
			</div>
		</div>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		width: 100%;
		height: 100%;

		top: 0;
		left: 0;
		position: fixed;
	}

	.background
	{
		width: 100%;
		height: 100%;
		cursor: pointer;
		backdrop-filter: blur(2px);
	}

	.content
	{
		width: 380px;
		height: 100%;
		box-shadow: -30px 0 80px 0 rgba(#000000, 0.5);
		border-left: 1px solid $light-gray;
		background-color: $darkest-gray;


		top: 0;
		right: 0;
		position: absolute;
	}

	.header
	{
		padding: 23px 26px;
		border-bottom: 1px solid $light-gray;

		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.title
	{
		color: $gray;
		font-size: 11px;
		font-weight: 600;
		letter-spacing: 1.76px;
		text-transform: uppercase;
	}

	.close
	{
		color: $white;
		padding: 14px;
	}

	.body { padding: 18px 14px 0 14px; }

	.body-title-wrapper
	{
		padding: 14px 12px 0 12px;
		margin-bottom: 8px;
	}

	.body-title
	{
		color: $light-gray-text;
		font-size: 10px;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 1.8px;
	}
</style>