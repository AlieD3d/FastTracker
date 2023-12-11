from rest_framework.serializers import ValidationError


def check_value_validate(value, inst_class=None):
    if not str(value).isdecimal():
        raise ValidationError(
            f'{value} должно содержать цифру'
        )
    if inst_class:
        obj = inst_class.objects.filter(id=value)
        if not obj.exists():
            raise ValidationError(
                f'{value} не существует'
            )
        return obj[0]
