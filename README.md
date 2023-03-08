# Django-Ninja
 Project API with Django Ninja Para Rodar o Back-End

# Este projeto foi feito com:

* asgiref 3.6.0
* Django 4.1.7
* django-cors-headers 3.14.0
* django-ninja 0.21.0
* Pillow 9.4.0
* pydantic 1.10.5
* sqlparse 0.4.3
* typing_extensions 4.5.0
* tzdata 2022.7

# Como rodar o projeto?
~~~linux
git clone https://github.com/santosgv/Django-Ninja.git
cd Django-Ninja
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
python manage.py runserver
