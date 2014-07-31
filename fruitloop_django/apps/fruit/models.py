from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class FruitType(TimeStampedModel):

    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Fruit Types"

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)


class FruitLocation(TimeStampedModel):

    address = models.CharField(
        max_length=50)
    comment = models.TextField(
        blank=True, null=True)
    fruit_type = models.ForeignKey(FruitType)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=7,
        blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7,
        blank=True, null=True)

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Fruit Locations"

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s tree at %s' % (self.fruit_type, self.address)
