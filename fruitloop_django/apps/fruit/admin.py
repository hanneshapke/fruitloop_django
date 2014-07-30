from django.contrib.gis import admin
from .models import FruitLocation


class FruitLocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    list_display = (
        'get_fruit_type_display', 'address',
        'modified',)


admin.site.register(FruitLocation, FruitLocationAdmin)
