import { clientSerializer } from "~/utils/serializers/clientSerializer";

const { clients: clientsApi } = useApi();

export const useClientsStore = defineStore('clients', () =>
	{
		const clients = ref([]);

		const getClients = async () =>
		{
			const response = await clientsApi.getClients()
			setClients(response);
		};

		const setClients = (data) => clients.value = data.map(client => clientSerializer(client));

		return {
			clients,

			getClients,
			setClients
		}
	}
)