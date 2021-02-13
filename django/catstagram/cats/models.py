from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
