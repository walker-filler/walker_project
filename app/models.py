from typing import Any
from django.db import models


# Create your models here.
class Product(models.Model):
    item = models.CharField(max_length=255, unique=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.item
