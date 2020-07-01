from django.test import TestCase
from .models import *
from datetime import date
# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        self.userValid=User(
                firstname="lion", 
                lastname="roar",
                email="kemuel.kany@live.fr",
                password="password01",
                dateDeNaissance=date.today().replace(year=date.today().year-20),
        )

    def testFirstname(self):
        """
        FirstNAme existe
        """
        self.assertTrue(self.userValid.firstname!=None)
    
    def testLastname(self):
        """
        lastname existe
        """
        self.assertTrue(self.userValid.lastname!=None)

    def testEmail(self):
        """
        Email Valide
        """
        userNonValide=User(
                firstname="lion", 
                lastname="roar",
                email="kemuel.kanylive.fr",
                password="password01",
                dateDeNaissance=date.today().replace(year=date.today().year-20),
        )

        self.assertEqual(userNonValide.isValid(),False)
        self.assertEqual(self.userValid.isValid(),True)

    def testAge(self):
        """
        age superieur a 13 ans
        """
        userNonValide=User(
                firstname="lion", 
                lastname="roar",
                email="kemuel.kany@live.fr",
                password="password01",
                dateDeNaissance=date.today().replace(year=date.today().year-12),
        )

        self.assertEqual(userNonValide.isValid(),False)
        self.assertEqual(self.userValid.isValid(),True)

    