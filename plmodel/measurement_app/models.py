from django.db import models


class EnvoronmentCondition(models.Model):
    temp = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField(default=60, blank=False)

    class Meta:
        unique_together = ('temp', 'pressure', 'humidity')

    def __str__(self):
        pressure = 'vacuum'
        if self.pressure > 1:
            pressure = 'room'
        temp = str(int(self.temp)) + 'C'

        lst = map(str, [temp, pressure, str(int(self.humidity)) + '%'])
        return '_'.join(lst)


class CodeOfMeasurement(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=False)

    def __str__(self):
        return self.code


class Measurement(models.Model):
    code = models.ForeignKey(CodeOfMeasurement,
                             on_delete=models.CASCADE)
    equipment = models.ForeignKey('equipment_app.EquipmentSetup',
                                  on_delete=models.CASCADE)
    env_condition = models.ForeignKey(EnvoronmentCondition,
                                      on_delete=models.CASCADE)
    data = models.TextField(blank=False)

    class Meta:
        unique_together = ('code', 'env_condition', 'equipment')

    def __str__(self):
        return '#'.join([str(self.code), str(self.equipment), str(self.env_condition)])
