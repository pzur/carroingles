from django.db import models
from django.contrib.auth.models import User


class People(models.Model):
    # Clientes,Despachador,Administrador,Operador
    adress = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    ruc = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='People/Fotos', null=True, blank=True)
    status = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='People')
    

    def __str__(self):
        return str(self.email)


class Cards(models.Model):
    cardname = models.CharField(max_length=300, null=True, blank=True)
    cardnumber = models.CharField(max_length=30, null=True, blank=True)
    cardcvv = models.IntegerField(null=True, blank=True)
    cardexp = models.DateField(null=True, blank=True)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cardname)

