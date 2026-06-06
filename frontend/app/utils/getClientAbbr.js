export default (str, maxLength = 2) =>
{
	if (!str || typeof str !== 'string') return '';

	const cleanStr = str.trim();
	if (!cleanStr) return '';

	const upperCaseLetters = cleanStr.match(/[A-ZА-ЯЁ]/g);

	if (upperCaseLetters && upperCaseLetters.length >= 2)
		return upperCaseLetters.slice(0, maxLength).join('');

	const words = cleanStr.split(/\s+/);
	let abbr    = '';

	for (const word of words)
	{
		if (abbr.length >= maxLength)
			break;

		const firstChar = word.charAt(0).toUpperCase();

		if (/[A-ZА-ЯЁ]/.test(firstChar))
			abbr += firstChar;
	}

	if (abbr.length >= 2)
		return abbr.slice(0, maxLength);

	const lettersOnly = cleanStr.replace(/[^A-ZА-ЯЁa-zа-яё]/g, '');
	return lettersOnly.substring(0, maxLength).toUpperCase();
}