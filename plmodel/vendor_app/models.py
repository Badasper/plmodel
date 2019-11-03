from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    short_name = models.CharField(max_length=10, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    info = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '-'.join([self.short_name, str(self.country)[0].upper()])
