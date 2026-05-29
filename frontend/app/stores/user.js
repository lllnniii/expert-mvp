import { userSerializer } from "~/utils/serializers/userSerializer";

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

		const setUserData = (value) => user.value = value;

		const getCurrentUser = async () =>
		{
			const response = await account.getCurrentUser();
			setUserData(userSerializer(response));
		}

		const logout = async (refreshToken) => await account.logout(refreshToken);

		return {
			user,

			setUserData,

			login,
			logout,
			registration,
			getCurrentUser
		}
	}
)