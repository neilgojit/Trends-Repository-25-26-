from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lasttname = models.CharField(max_length=255)
    