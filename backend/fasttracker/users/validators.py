from re import compile

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RegexpStringValidator:
    first_regexp = '[^а-яёА-ЯЁ]+'
    second_regexp = '[^a-zA-Z]+'
    error_message = (
        'Поле содержит буквы на разных языках или содержит недопустимые символы'
    )

    def __init__(self, f_reg=None, s_reg=None):
        if f_reg is not None:
            self.first_regexp = f_reg
        if s_reg is not None:
            self.second_regexp = s_reg

        self.first_regexp = compile(self.first_regexp)
        self.second_regexp = compile(self.second_regexp)

    def __call__(self, value):
        if (self.first_regexp.search(value)
                and self.second_regexp.search(value)):
            raise ValidationError(self.error_message)


@deconstructible
class MinLenUsernameValidator:
    min_len = 0
    error_message = 'Слишком короткое имя!'

    def __init__(self, min_len=None, message=None):
        if min_len is not None:
            self.min_len = min_len
        if message is not None:
            self.error_message = message

    def __call__(self, value):
        if len(value) < self.min_len:
            raise ValidationError(self.error_message)
