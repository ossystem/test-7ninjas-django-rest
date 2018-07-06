Install requirements:
```
pip install -r requirements.txt
```

Run tests:
```
python manage.py test api
```

Create DB structure:
```
python manage.py migrate
```

Create superuser:
```
python manage.py createsuperuser
```

And finally run server:
```
python manage.py runserver
```

API root will be available at http://localhost:8000/api/
