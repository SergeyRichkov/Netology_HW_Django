from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    slug = models.SlugField()
    lte_exists = models.BooleanField(default=False)

