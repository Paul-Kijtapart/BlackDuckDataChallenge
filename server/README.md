# Server

### Set up PostgreSQL Database:

1. Install PostgreSQL
```
brew update
brew install postgres
postgres -D /usr/local/var/postgres
psql
```

2. Install psycopg2
```
pip install psycopg2
```

3. Create database name "blackduck" and user with Createdb permission
```
CREATE DATABASE blackduck;
CREATE USER blackduckuser WITH PASSWORD 'blackduckpassword';
GRANT ALL PRIVILEGES ON DATABASE "blackduck" to tester;
```

4. Creates a file name "secret_config.py" in server/server
```
For example,
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blackduck',
        'USER': 'blackduckuser',
        'PASSWORD': 'blackduckpassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

5. Initialize Environment
```
python manage.py makemigrations
python manage.py migrate
```

6. Load initial data
```
python manage.py load_initial_data
python manage.py display_initial_data
```

## Run Locally
```
python manage.py runserver
```
