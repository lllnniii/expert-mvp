export default {
	getObjects: async () => await useRequest('/objects'),

	addObject: async (payload) => await useRequest('/objects',
		{
			method: 'POST',
			body:
			{
				client_id      : payload.clientId,
				description    : payload.description,
				object_name    : payload.objectName,
				opos_category  : payload.oposCategory,
				object_address : payload.objectAddress
			}
		}
	),

	deleteObject: async (id) => await useRequest(`/objects/${id}`, { method: 'DELETE' }),

	changeObject: async (payload) => await useRequest(`/objects/${payload.id}`,
		{
			method: 'PATCH',
			body:
			{
				description    : payload.description,
				object_name    : payload.name,
				opos_category  : payload.oposCategory,
				object_address : payload.address
			}
		}
	)
}