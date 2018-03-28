SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "core",
    "core.tests",
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}