from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class FruitLocation(TimeStampedModel):

    FRUIT_CHOICES = (
        ('cherry', 'Cheery'),
        ('apple', 'Apples'),
        ('other', 'Other'),
    )
    address = models.CharField(
        max_length=50)
    comment = models.TextField(
        blank=True, null=True)
    fruit_type = models.CharField(
        choices=FRUIT_CHOICES,
        max_length=20)
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
        return '%s tree at %s' % (self.get_fruit_type_display(), self.address)
