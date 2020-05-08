from django.db import models
from validate_email import validate_email
from datetime import date, timedelta


class User(models.Model):
    firstname = models.CharField(max_length=200,verbose_name="firstname")
    lastname = models.CharField(max_length=200,verbose_name="lastName")
    email = models.CharField(max_length=200,verbose_name="email")
    password = models.CharField(max_length=200,verbose_name="password")
    dateDeNaissance = models.DateField(verbose_name="nom du manga")
    todo= models.ForeignKey('ToDoList',null=True,blank=True,on_delete=models.PROTECT,related_name="u_todolist",verbose_name="todos liste")

    def __str__(self):
        return self.firstname

    def isValid(self):
        return validate_email(self.email) and \
                self.firstname !=None and \
                self.lastname !=None and \
                len(self.password) >= 8 and \
                len(self.password) <= 40 and \
                ((date.today() - self.dateDeNaissance) // timedelta(days=365.2425) > 13)

class ItemToDoList(models.Model):
    i_title = models.CharField(max_length=200,verbose_name="titre de l'items")
    i_date =models.DateTimeField(verbose_name="nom du manga",blank=True,null=True)

    def __str__(self):
        return self.i_title

class ToDoList(models.Model):
    t_titre = models.CharField(max_length=200,verbose_name="titre de la todo")
    t_todoList= models.ForeignKey('ToDoList',null=True,blank=True,on_delete=models.PROTECT,related_name="t_items",verbose_name="User de la todos liste")
    t_listeItems =models.ManyToManyField(ItemToDoList,blank=True)
    
    
    def __str__(self):
        return self.t_titre
    
    def canAddItem(self,items):
        if len(self.t_listeItems.all())<10:
            if len(self.t_listeItems.all())!=0:
                lastCreate=self.t_listeItems.all().latest('i_date')
                timeBetweeen=items.i_date.replace(tzinfo=None) - lastCreate.i_date.replace(tzinfo=None)
                duration_in_s = timeBetweeen.total_seconds() 
                if (duration_in_s/60 > 30 ):
                    items.save()
                    self.t_listeItems.add(items)
                    return "OK"
            else:
                items.save()
                self.t_listeItems.add(items)
                return "OK"
        return None

# Create your models here.
