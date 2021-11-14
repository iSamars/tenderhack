from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    tg_id = models.CharField(max_length=25)
    chat_id = models.CharField(max_length=25)
