from django.test import TestCase
from .models import *
from datetime import date,datetime
# Create your tests here.

class TodoListTest(TestCase):
    """
    test de la table User
    """
    def setUp(self):
        self.userValid=User(
                firstname="lion", 
                lastname="roar",
                email="kemuel.kany@live.fr",
                password="password01",
                dateDeNaissance=date.today().replace(year=date.today().year-20),
        )
        self.maTodoList=ToDoList(
            t_titre="Ma premiere"
        )
        self.userValid.todo=self.maTodoList
        self.maTodoList.save()
        self.userValid.save()

    def testContentMax(self):
        """
        Pas plus de 10 elements
        """
        date=datetime.now()
        #date=date + timedelta(min==31) 
        for i in range(0,20):
            self.maTodoList.canAddItem(
                ItemToDoList(
                    i_title=(str(i)+" item"),
                    i_date=date
                )
            )
            date=date + timedelta(seconds=(60*30)) 
        self.assertEqual(len(self.maTodoList.t_listeItems.all()),10)

    def testMinBefefore(self):
        """
        Pas moins de 30 minute depuis la derniere creations
        """
        date=datetime.now()
        #date=date + timedelta(min==31) 
        for i in range(0,10):
            self.maTodoList.canAddItem(
                ItemToDoList(
                    i_title=(str(i)+" item"),
                    i_date=date
                )
            )
            date=date + timedelta(seconds=(60*28)) 
        self.assertEqual(len(self.maTodoList.t_listeItems.all()),5)