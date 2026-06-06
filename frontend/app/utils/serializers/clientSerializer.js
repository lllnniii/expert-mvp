export const clientSerializer = (client) =>
{
	if (!client.client_id) return {};

	return {
		id            : client.client_id,
		inn           : client.inn,
		name          : client.client_name,
		email         : client.contact_email,
		fullName      : client.full_name,
		addressLegal  : client.address_legal,
		contactPhone  : client.contact_phone,
		addressActual : client.address_actual,
		contactPerson : client.contact_person
	}
};