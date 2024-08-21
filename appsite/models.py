from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by' + str(self.user)



class sitename(models.Model):
    site = models.CharField(max_length=100)
    mim = models.CharField(max_length=100)
    siteid = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class sitetipos(models.Model):
    tipo = models.CharField(max_length=10)
    site_id=models.ForeignKey(sitename, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)