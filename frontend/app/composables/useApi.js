import account from "~/api/account";
import clients from "~/api/clients";
import objects from "~/api/objects";

export const useApi = () =>
{
	return {
		account,
		clients,
		objects
	};
}