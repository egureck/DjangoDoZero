from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustumUser(AbstractUser):
    dt_nasc = models.DateField(
        "Data de Nascimento",
        null=True,
        blank=True  
    )
    cpf = models.CharField(
        "CPF",
        max_length=11,
        null=True,
        blank=True
    )