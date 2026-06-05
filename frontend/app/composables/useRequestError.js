export const useRequestError = (error, showToast = true) => {
	const toastsStore = useToastsStore();

	const detail = error.data?.detail;
	let message  = 'Произошла неизвестная ошибка';

	if (detail) {
		if (Array.isArray(detail))
		{
			message = detail
				.map(item => item?.msg ?? String(item))
				.join('; ');
		}
		else if (typeof detail === 'object' && 'msg' in detail)
			message = detail.msg;
		else
			message = typeof detail === 'string' ? detail : JSON.stringify(detail);
	}

	if (showToast && toastsStore && detail)
		toastsStore.addToast(message, 'error');

	console.error(error);
};