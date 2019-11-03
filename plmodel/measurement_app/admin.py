from django.contrib import admin
from . import models


admin.site.register(models.Measurement)
admin.site.register(models.EnvoronmentCondition)
admin.site.register(models.CodeOfMeasurement)
