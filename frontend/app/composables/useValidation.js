import { required, minLength, withMessage } from '@regle/rules';

export function useValidation() {
	const requiredField = (field, message) => {
		return {
			[field]: { required: withMessage(required, message) }
		};
	};

	const passwordField = (
		field           = 'password',
		requiredMessage = 'Пароль обязателен',
		invalidMessage  = 'Минимум 6 символов'
	) => {
		return {
			[field]: {
				required  : withMessage(required, requiredMessage),
				minLength : withMessage(minLength(6), invalidMessage)
			}
		}
	}

	return {
		passwordField,
		requiredField
	};
}
