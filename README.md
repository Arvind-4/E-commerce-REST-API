# E-commerce-REST-API

### Get the Code

- Clone Repo

```
mkdir ecommerce
cd ecommerce
git clone https://github.com/Arvind-4/E-commerce-REST-API.git .
```
- Create Virtual Environment for Python

```
pip install virtualenv
python -m venv .
```

- Activate Virtual Environment

```
source Scripts/activate
```

- Install Dependencies

```
pip install -r requirements.txt
```


- db migrations

```
python manage.py makemigrations
python manage.py migrate
```


- Run Server 
```
python manage.py runserver
```

Visit [localhost:8000](http://localhost:8000) .
