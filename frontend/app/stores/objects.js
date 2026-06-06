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

		const addObject = (object) => objects.value.push(object);

		const updateObject = (updatedObject) =>
		{
			const serializedObject = objectSerializer(updatedObject);
			const index            = objects.value.findIndex(obj => obj.id === serializedObject.id);

			if (index !== -1)
				objects.value[index] = serializedObject;
			else
				objects.value.push(serializedObject);
		};

		return {
			objects,

			addObject,
			getObjects,
			setObjects,
			updateObject
		}
	}
);