<template>
	<div class="wrapper">
		<span class="loader"></span>
	</div>
</template>

<style scoped lang='scss'>
	.wrapper
	{
		width: 100%;
		height: 100%;
		backdrop-filter: blur(4px);
		background-color: rgba($primary, 0.5);

		top: 0;
		left: 0;
		display: flex;
		position: fixed;
		align-items: center;
		justify-content: center;
	}

	.loader {
		color: $green;
		width: 40px;
		height: 40px;
		animation: loader 1.5s infinite cubic-bezier(0.3,1,0,1);
		background:
			conic-gradient(from  -45deg at top    20px left 50% ,#0000 ,currentColor 1deg 90deg,#0000 91deg),
			conic-gradient(from   45deg at right  20px top  50% ,#0000 ,currentColor 1deg 90deg,#0000 91deg),
			conic-gradient(from  135deg at bottom 20px left 50% ,#0000 ,currentColor 1deg 90deg,#0000 91deg),
			conic-gradient(from -135deg at left   20px top  50% ,#0000 ,currentColor 1deg 90deg,#0000 91deg);
	}

	@keyframes loader {
		50%
		{
			width:60px;
			height: 60px;
			transform: rotate(180deg)
		}
		100% { transform: rotate(360deg) }
	}
</style>