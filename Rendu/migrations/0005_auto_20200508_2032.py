# Generated by Django 3.0.6 on 2020-05-08 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0004_itemtodolist_todolist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtodolist',
            name='i_todoList',
        ),
        migrations.AddField(
            model_name='todolist',
            name='t_listeItems',
            field=models.ManyToManyField(blank=True, null=True, to='Rendu.ItemToDoList'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='t_todoList',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='t_items', to='Rendu.ToDoList', verbose_name='User de la todos liste'),
        ),
    ]
