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

	deleteObject: async (id) => await useRequest(`/objects/${id}`, { method: 'DELETE' })
}