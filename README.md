# How to setup the project

1. Create virtual environment and activate

```cmd
    python -m venv .venv
    .venv/Script/activate
```

2. Install requirments.txt (python 3.11 is used here)

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

5. To access swagger UI goto `api/` endpoint