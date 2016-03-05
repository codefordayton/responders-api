# responders-api
API for disaster recovery first responders

# Development

Set up an initial development environment (assuming Docker and VirtualEnv installed):

```
bash init-dev.sh
source .env/bin/activate
```

Create an admin superuser, initialize geocoding data and start the server:

```
python manage.py createsuperuser
python manage.py loaddata geocode
python manage.py runserver
```
