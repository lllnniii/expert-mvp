const { account } = useApi();

export const useUserStore = defineStore('user', () =>
	{
		const user = ref(null);

		const login = async (payload) =>
		{
			const response = await account.login(payload);
			return response;
		}

		const registration = async (payload) =>
		{
			const response = await account.registration(payload);
			return response;
		}

		return {
			user,

			login,
			registration
		}
	}
)