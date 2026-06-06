export default (oposCategory) =>
{
	switch (oposCategory) {
		case '1 Класс':
			return 'violet'
		case '2 Класс':
			return 'red'
		case '3 Класс':
			return 'yellow'
		case '4 Класс':
			return 'green'
		default:
			break;
	};
};