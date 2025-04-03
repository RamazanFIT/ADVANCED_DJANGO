INSTALLED_APPS += [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_filters',
    'expenses',
]

LOGIN_REDIRECT_URL = 'expenses:expense_list'
LOGIN_URL = 'login' 