def get_plural_form_number(number: int, forms: tuple):
    """get_plural_form_number(minutes, ('минуту', 'минуты', 'минут'))"""
    if number % 10 == 1 and number % 100 != 11:
        return forms[0]
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return forms[1]
    else:
        return forms[2]


def get_user_by_email_or_name(email_or_name: str) -> Tuple[Optional[User], str]:
    """Если пользователь не найден вернется None и строка ошибки, иначе User и пустая строка"""
    user_ = None
    error = ''
    if '@' in email_or_name:
        try:
            user_ = User.objects.get(email=email_or_name)
        except User.DoesNotExist:
            error = USER_EMAIL_NOT_EXISTS
    else:
        try:
            user_ = User.objects.get(username=email_or_name)
        except User.DoesNotExist:
            error = USER_USERNAME_NOT_EXISTS

    return user_, error