from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='category/Photos', null=True, blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name="categoria")

    def __str__(self):
        return self.name
