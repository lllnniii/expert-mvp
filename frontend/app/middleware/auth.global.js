export default defineNuxtRouteMiddleware((to) =>
	{
		const toPath = to.fullPath;
		const token  = useCookie('promTokenAccess');

		if (!token.value && (toPath !== '/login' && toPath !== '/registration'))
			return navigateTo('/login');

		if (toPath === '/login' || toPath === '/registration')
			token.value = '';
	}
);