from django.db import models


class LinkedinUsers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    about = models.CharField(max_length=500)
    experiences = models.TextField()
    contacts = models.TextField()
