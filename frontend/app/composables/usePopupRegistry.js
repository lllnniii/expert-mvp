import AddObject from "~/components/popups/AddObject/index.vue";

const popups = { 'addObject' : AddObject };

export const usePopupsRegistry = (name) =>
{
	if (!name) return;

	return popups[name];
}