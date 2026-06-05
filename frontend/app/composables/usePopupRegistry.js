import AddObject from "~/components/popups/AddObject.vue";

const popups = { 'addObject' : AddObject };

export const usePopupsRegistry = (name) =>
{
	if (!name) return;

	return popups[name];
}