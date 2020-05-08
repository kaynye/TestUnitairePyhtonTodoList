#TODO List Test Unitaire


#Instalation
Pour lancer le projet
Installer le 'environnement django et les modules neccessaire
    pyhton install -r requirement.txt

Mettre en place la base de données
dans TodoList/setting.py
configurer votre base de donnée 

```
DATABASES = {
    'default': {
        'OPTIONS' : {
            'options': '-c search_path=django,public'
        },
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'TestUnit', # le nom de notre base de donnees creee precedemment
        'USER': 'postgres', # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    },
}
```python

creer ensuite les tables de l'appliction
    python manage.py migrate # les migrations ont deja été appliquées dans le projet

lancer les tests du projet:
    #pour les table todoList
    python manage.py test testTodoList
    #pour les table User
    python manage.py test testTodoUser
