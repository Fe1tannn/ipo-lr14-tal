from django.db import models

class Establishment(models.Model):
    id = models.IntegerField(primary_key=True)  # Переименовано pk в id
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=50)
    desc = models.TextField()
    adress = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    wsite = models.URLField(null=True, blank=True)
    wtel = models.URLField(null=True, blank=True)
    wvk = models.URLField(null=True, blank=True)
    winsta = models.URLField(null=True, blank=True)
    wface = models.URLField(null=True, blank=True)
    wtwit = models.URLField(null=True, blank=True)
    wtic = models.URLField(null=True, blank=True)
    wother = models.URLField(null=True, blank=True)
    icon = models.CharField(max_length=100)
    prev = models.CharField(max_length=100, blank=True)
    promo_medio = models.CharField(max_length=100, blank=True)
    coords = models.CharField(max_length=50)

    def __str__(self):
        return self.title