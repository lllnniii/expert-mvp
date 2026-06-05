import { required, minLength, email as emailRule, withMessage } from '@regle/rules';

export function useValidation() {
	const requiredField = (field, message) =>
	{
		return { [field]: { required: withMessage(required, message) } };
	};

	const minLengthField = (field, message, length) =>
	{
		return { [field]: { minLength: withMessage(minLength(length), message) } }
	};

	const emailField = (
		field           = 'email',
		requiredMessage = 'Укажите e-mail',
		invalidMessage  = 'Укажите корректный e-mail'
	) =>
	{
		return {
			[field]:
			{
				required: withMessage(required, requiredMessage),
				email   : withMessage(emailRule, invalidMessage),
			},
		};
	};

	const phoneField = (
		field           = 'phone',
		requiredMessage = 'Укажите телефон',
		invalidMessage  = 'Некорректный формат телефона'
	) =>
	{
		return {
			[field]:
			{
				required : withMessage(required, requiredMessage),
				minLength: withMessage(minLength(16), invalidMessage),
			},
		};
	};

	const passwordField = (
		field           = 'password',
		requiredMessage = 'Пароль обязателен',
		invalidMessage  = 'Минимум 6 символов'
	) =>
	{
		return {
			[field]:
			{
				required  : withMessage(required, requiredMessage),
				minLength : withMessage(minLength(6), invalidMessage)
			}
		}
	}

	return {
		phoneField,
		emailField,
		passwordField,
		requiredField,
		minLengthField
	};
}
