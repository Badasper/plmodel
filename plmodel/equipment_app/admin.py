from django.contrib import admin
from . import models


admin.site.register(models.Equipment)
admin.site.register(models.TypeOfEquipment)
admin.site.register(models.EquipmentSetup)
