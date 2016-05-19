Pràctica II Govern de les TIC
===

## Instalación

El proyecto está realizado con Django v1.9 y Python v2.7.

Para desarrollar en este proyecto hemos instalado el siguiente software:

* git
* mysql-server
* mysql-client
* python-pip
* python-mysqldb

También hay que instalar todo lo que haya recogido dentro del archivo requirements.txt mediante
```
pip install requirements.txt
```

De cara al deploy y a la página web de [!](govern.herokuapp.com) hemos hosteado la aplicación en Heroku mediante una cuenta de usuario básica. En ella hemos creado una nueva aplicación y la hemos conectado con nuestro repositorio de GitHub para que los deploys se hagan automáticamente al subir cambios a `master`.

En Heroku hemos utilizado el paquete básico de PostgreSQL como base de datos del servidor, sin embargo, en local hemos utilizado MySQL.

Para desarrollar en **local** la base de datos tiene que cumplir los requisitos recogidos en el siguiente diccionario de `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'govern', # Nombre de la BD
        'USER': 'djangovern', # Usuario de la BD
        'PASSWORD': 'atupDmFCqhLWLmBs', # Password del usuario anterior
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Estos datos pueden adaptarse libremente a las necesidades de cada uno, sólo hay que asegurarse que en la BD de MySQL coinciden las credenciales del diccionario anterior.

Para crear una BD en mysql y darle acceso a un usuario con las credenciales anteriores
```
mysql> create database govern;
mysql> grant all on govern.* to 'govern'@'localhost' identified by 'atupDmFCqhLWLmBs';
```

Finalmente, podemos ejecutar una versión local del proyecto ejecutando en la raíz del proyecto
```
python manage.py migrate
python manage.py runserver
```
Seguidamente vamos a `localhost:8000` y veremos nuestra aplicación.

En **remoto** simplemente debemos subir nuestros cambios  la rama de master y la sincronización se hará automáticamente.

