export default {
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
	)
}