export const useToastsStore = defineStore('toasts', () =>
	{
		const toasts  = ref([]);
		const toastId = ref(0);

		const addToast = (text, variant) =>
		{
			const timeForRemoveMs = 3000;
			const currentToastId = toastId.value;

			toasts.value.push(
				{
					id      : currentToastId,
					variant : variant,
					text    : text
				}
			);

			setTimeout(() => removeToast(currentToastId), timeForRemoveMs)

			toastId.value += 1;
		};

		const removeToast = (id) => toasts.value = toasts.value.filter(toast => toast.id !== id);

		return {
			toasts,

			addToast,
			removeToast
		};
	}
);