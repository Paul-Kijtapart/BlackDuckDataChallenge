# Server

### Set up PostgreSQL Database:

1. Install PostgreSQL
brew update
brew install postgres
postgres -D /usr/local/var/postgres
psql

2 Install psycopg2
pip install psycopg2

3. Create database name "blackduck" and user with Createdb permission
CREATE DATABASE blackduck;
CREATE USER blackduckuser WITH PASSWORD 'blackduckpassword';
GRANT ALL PRIVILEGES ON DATABASE "blackduck" to tester;

4. Creates a file name "secret_config.py" in server/server
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

5. Initialize Environment
python manage.py makemigrations
python manage.py migrate


5.1 Load initial data
python manage.py load_initial_data
python manage.py display_initial_data

6. Perform Migration to let Django to set up environment
python manage.py migrate

## Run Locally
python manage.py runserver
