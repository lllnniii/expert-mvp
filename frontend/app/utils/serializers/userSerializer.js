export const userSerializer = (user) =>
{
	return {
		id        : user.account_id,
		name      : user.username,
		isActive  : user.is_active,
		createdAt : user.created_at,
		lastLogin : user.last_login_at
	};
};