export const useRequestError = (error, showToast = true) =>
{
	let toastsStore = showToast ? useToastsStore() : null;

	if (toastsStore && error.data?.detail)
		toastsStore.addToast(error.data?.detail, 'error');

	console.error(error);
};