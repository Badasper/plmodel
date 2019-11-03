from django.db import models
from vendor_app.models import Vendor


class TypeOfEquipment(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=150)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    serial_number = models.CharField(max_length=50, blank=False)
    type_of_equipment = models.ForeignKey(TypeOfEquipment,
                                          on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('serial_number', 'type_of_equipment')

    def __str__(self):
        return '#'.join([str(self.type_of_equipment), str(self.vendor), self.serial_number])


class EquipmentSetup(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    configuration = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return '@'.join(map(str, [self.equipment, self.configuration]))
