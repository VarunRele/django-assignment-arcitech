# How to setup the project

1. Create virtual environment and activate

```cmd
    python -m venv .venv
    .venv/Script/activate
```

2. Install requirments.txt

```cmd
    pip install -r requirments.txt
```

3. Setup the database run running migration commands

```cmd
    python manage.py migrate
```

4. Run following command to preload the data.
    This will create admin user and some categories
```cmd
    python manage.py seed
```
```
    admin = admin
    password = AdminPassword1
```

5. To access swagger UI goto `swagger/` endpoint

6. Create token by submitting as `application/json` type in swagger.

7. Authorization header
```python
    {'Authorization': f'Token {user_token}'}
```

8. Versions -
```
    python = "3.10.16"
    django = "^5.1.5"
    djangorestframework = "^3.15.2"
    faker = "^33.3.1"
    drf-spectacular = "^0.28.0"
```
