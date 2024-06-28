from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point, Polygon

class Country(models.Model):
    name = models.CharField(max_length=60)
    location = models.PolygonField()#default= Polygon(((0,0), (0,1), (1,1), (1,0), (0, 0))))
    country_city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='countries',null=True)
    country_capital = models.OneToOneField('Capital', on_delete=models.CASCADE, related_name='country',null=True)

    def __str__(self):
       return self.name

class City(models.Model):
    name = models.CharField(max_length=60)
    description=models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to = "images/")
    location = models.PointField()#default= Point(0,0))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', null=True)


    def __str__(self):
        return self.name



class Capital(models.Model):
    name = models.CharField(max_length=60)
    location = models.PointField()#default= Point(0,0))
    def __str__(self):
        return self.name



