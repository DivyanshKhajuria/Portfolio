from django.db import models

# Create your models here.
class Mymessage(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subj=models.CharField(max_length=200)
    youmsg=models.TextField(max_length=200)

