import { clientSerializer } from "./clientSerializer";

export const objectSerializer = (object) =>
{
	return {
		id           : object.object_id,
		name         : object.object_name,
		address      : object.object_address,
		description  : object.description,
		oposCategory : object.opos_category,
		client       : object.clients ? clientSerializer(object.clients) : null
	}
};