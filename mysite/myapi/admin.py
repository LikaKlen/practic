from django.contrib import admin
from django.contrib.gis import admin
from .models import City
from .models import Country
from .models import Capital
admin.site.register(City,admin.OSMGeoAdmin)
admin.site.register(Country,admin.OSMGeoAdmin)
admin.site.register(Capital,admin.OSMGeoAdmin)