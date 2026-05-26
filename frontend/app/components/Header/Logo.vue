<template>
	<NuxtLink to="/" class="logo-wrapper">
		<IconsLogo class="icon" />
		<div>
			<p class="title">PromExpert</p>
			<p class="description">Industrial Safety</p>
		</div>
	</NuxtLink>
</template>

<style scoped lang='scss'>
	.logo-wrapper
	{
		column-gap: 12px;

		display: flex;
		align-items: center;
	}

	.icon { color: #23E07B; }

	.title
	{
		font-size: 18px;
		font-weight: 800;
		margin-bottom: 1px;
		letter-spacing: -0.38px;
	}

	.description
	{
		color: $gray;
		font-size: 11px;
		font-weight: 500;
		letter-spacing: 1.54px;
		text-transform: uppercase;
	}

</style>