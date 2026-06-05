export const usePopupsStore = defineStore('popups', () =>
	{
		const activePopup = ref(null);
		const popupData   = ref(null);

		const togglePopup = (name, value) =>
		{
			if (value)
				activePopup.value = name
			else
			{
				activePopup.value = null;
				setPopupData(null);
			}
		};

		const closeCurrentPopup = () =>
		{
			activePopup.value = null;
			setPopupData(null);
		};

		const setPopupData = (data) => popupData.value = data;

		return {
			popupData,
			activePopup,

			togglePopup,
			setPopupData,
			closeCurrentPopup
		}
	}
);