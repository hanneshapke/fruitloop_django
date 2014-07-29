from django.contrib.auth.models import User
from django.contrib.gis.db import models
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
    location = models.PointField(
        srid=4326, blank=True, null=True)

    objects = models.GeoManager()

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Fruit Locations"

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s tree at %s' % (self.get_fruit_type_display(), self.address)
