import { objectSerializer } from "~/utils/serializers/objectSerializer";

const { objects: objectsApi } = useApi();

export const useObjectsStore = defineStore('objects', () =>
	{
		const objects = ref([]);

		const getObjects = async () =>
		{
			const response = await objectsApi.getObjects();
			setObjects(response);
		};

		const setObjects = (data) => objects.value = data.map(object => objectSerializer(object));

		const addObject = (object) =>
			{
				objects.value.push(object)
				console.log(objects.value);
			};

		return {
			objects,

			addObject,
			getObjects,
			setObjects
		}
	}
);