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
	)
}