# Generated by Django 3.0.6 on 2020-05-08 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0002_itemtodolist_todolist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='t_user',
        ),
        migrations.DeleteModel(
            name='ItemToDoList',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
