from django.db import models


class AbstractActionType(models.Model):
    PRODUCES_RESULT_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    produces_result = models.CharField(db_column='producesResult', max_length=5, choices=PRODUCES_RESULT_CHOICES,
                                       blank=True)

    class Meta:
        abstract = True


class AbstractSpatialOffsetType(models.Model):
    offset1 = models.TextField(db_column='offset1', blank=True)
    offset2 = models.TextField(db_column='offset2', blank=True)
    offset3 = models.TextField(db_column='offset3', blank=True)

    class Meta:
        abstract = True


class AbstractUnitsType(models.Model):
    default_unit = models.CharField(db_column='defaultUnit', max_length=100, blank=True)
    dimension_symbol = models.CharField(db_column='dimensionSymbol', max_length=50, blank=True)
    dimension_length = models.IntegerField(db_column='dimensionLength', blank=True, null=True)
    dimension_mass = models.IntegerField(db_column='dimensionMass', blank=True, null=True)
    dimension_time = models.IntegerField(db_column='dimensionTime', blank=True, null=True)
    dimension_current = models.IntegerField(db_column='dimensionCurrent', blank=True, null=True)
    dimension_temperature = models.IntegerField(db_column='dimensionTemperature', blank=True, null=True)
    dimension_amount = models.IntegerField(db_column='dimensionAmount', blank=True, null=True)
    dimension_light = models.IntegerField(db_column='dimensionLight', blank=True, null=True)

    class Meta:
        abstract = True
