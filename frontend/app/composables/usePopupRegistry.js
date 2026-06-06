import AddObject from "~/components/popups/AddObject/index.vue";
import EditObject from "~/components/popups/EditObject.vue";

const popups =
{
	'addObject'  : AddObject,
	'editObject' : EditObject
};

export const usePopupsRegistry = (name) =>
{
	if (!name) return;

	return popups[name];
}