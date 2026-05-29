export default {
	login: async (payload) => await useRequest('/account/login',
		{
			method: 'POST',
			body: payload
		}
	),

	registration: async (payload) => await useRequest('/account/register',
		{
			method: 'POST',
			body:
			{
				username        : payload.username,
				hashed_password : payload.password
			}
		}
	),

	getCurrentUser: async () => await useRequest('/account/me'),

	logout: async (refreshToken) => await useRequest('/account/logout',
		{
			method: 'POST',
			body: { refresh_token: refreshToken }
		}
	)
}