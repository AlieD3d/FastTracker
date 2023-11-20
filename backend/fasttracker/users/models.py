from django.db import models
from django.db.models import CharField, CheckConstraint, Q
from django.db.models.functions import Length

from api import conf
from django.contrib.auth.models import AbstractUser

from users.validators import MinLenUsernameValidator, RegexpStringValidator

CharField.register_lookup(Length)


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        max_length=conf.MAX_LEN_EMAIL_CHAR,
        help_text=conf.USERS_HELP_EMAIL
    )
    username = CharField(
        max_length=conf.MAX_LEN_USERS_CHAR,
        unique=True,
        verbose_name='Имя пользователя',
        help_text=(conf.USERS_HELP_USERNAME,),
        validators=(
            MinLenUsernameValidator(min_len=conf.MIN_LEN_USERS_CHAR),
            RegexpStringValidator()
        ),
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=conf.MAX_LEN_USERS_CHAR,
        help_text=conf.USERS_HELP_FIRSTNAME
    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=conf.MAX_LEN_USERS_CHAR,
        help_text=conf.USERS_HELP_FIRSTNAME
    )
    password = CharField(
        verbose_name='Пароль',
        max_length=conf.MAX_LEN_USERS_CHAR
    )
    subscribe = models.ManyToManyField(
        verbose_name='Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False
    )

    def __str__(self):
        return f'{self.username}: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = (
            CheckConstraint(
                check=Q(username__length__gte=conf.MIN_LEN_USERS_CHAR),
                name='\nusername to longest!\n',
            ),
        )
