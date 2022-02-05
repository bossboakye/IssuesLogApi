#Issues Log Api is a mini ticketing tool to help log and track incidnets as they happen.

* Install the dependencies (preferably in a Virtual environment)
RUN 
```shell
$ pip3 install -r requirements.txt
```

* Edit settings.py DATABASE config with your Database config:
```php
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{DBName}',
        'USER': '{DBUser}',
        'PASSWORD': '{DBPassword}',
        'HOST': '{DBHostAddress}',
        'PORT': '{DBPort}'
    }
}
```

* Start the Server by running:
```shell
$ python3 manage.py runserver
```