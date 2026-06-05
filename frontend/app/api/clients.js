export default {
	getClients: async () => await useRequest('/clients'),

	createClient: async (payload) => await useRequest('/clients',
		{
			method: 'POST',
			body:
			{
				inn            : payload.inn,
				full_name      : payload.fullName,
				client_name    : payload.clientName,
				contact_phone  : payload.contactPhone,
				contact_email  : payload.contactEmail,
				address_legal  : payload.addressLegal,
				address_actual : payload.addressActual,
				contact_person : payload.contactPerson
			}
		}
	)
}