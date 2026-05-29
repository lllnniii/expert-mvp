export const useRequest = async (request, opts = {}) =>
{
	const config = useRuntimeConfig();
	const token = useCookie('promTokenAccess')

	const options =
	{
		baseURL: config.public.api,
		headers: { 'Authorization': token.value ? `Bearer ${token.value}` : null },
		...opts,
	};

	try { return await $fetch(request, options); }
	catch (e)
	{
		const errorObject =
			e?.response?._data ||
			e?.data ||
			'Request error';

			const err = new Error(`Request error: ${request}`);
			err.data = errorObject;

			throw err;
	}
};