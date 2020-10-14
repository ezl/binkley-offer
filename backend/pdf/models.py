from django.db import models
from django.contrib.auth.models import User

class Pdf(models.Model):
    redfin_src = models.TextField(unique=True)
    pdf_src = models.TextField()
    deleted = models.BooleanField(default=False)
    user_email = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_uid = models.TextField(unique=True)
    username = models.TextField()
    password = models.TextField()
    email = models.EmailField(unique=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)


class Token(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()
    user_id = models.BigIntegerField()
