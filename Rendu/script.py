from django.db import models
from validate_email import validate_email
from datetime import date, timedelta
from .models import *

u=User(
                firstname="lion", 
                lastname="roar",
                email="roar",
                password="roar",
                dateDeNaissance=date.today(),
        )