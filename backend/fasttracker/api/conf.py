DATE_TIME_FORMAT = '%d/%m/%Y %H:%M'

ADD_METHODS = ('GET', 'POST',)

DEL_METHODS = ('DELETE',)

ACTIONS_METHODS = [s.lower() for s in (ADD_METHODS + DEL_METHODS)]

UPDATE_METHODS = ('PUT', 'PATCH')

SEARCH_TASK_NAME = 'name'

SUBSCRIBE_M2M = 'subscribe'

FAVORITE_M2M = 'is_favorited'

AUTHOR = 'author'

TAGS = 'tags'

SYMBOL_TRUE_SEARCH = (1, True)

SYMBOL_FALSE_SEARCH = (0, False)

MAX_LEN_USERS_CHAR = 150

MIN_LEN_USERS_CHAR = 3

MAX_LEN_EMAIL_CHAR = 254

MAX_LEN_TASKS_CHAR = 200

MAX_LEN_TASKS_TEXT = 5000

USERS_HELP_EMAIL = (
    'Обязательно для заполнения.'
    f'Максимум {MAX_LEN_EMAIL_CHAR} букв.'
)

USERS_HELP_USERNAME = {
    'Обязательно для заполнения.'
    f'От {MIN_LEN_USERS_CHAR} ДО {MAX_LEN_USERS_CHAR} букв.'
}

USERS_HELP_FIRSTNAME = (
    f'Обязательно для заполнения. Максимум {MAX_LEN_USERS_CHAR} букв.'
)


