from rest_framework import serializers

from .models import City
from .models import Country
from .models import Capital

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name','description','photo','location')

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name','location')

class CapitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capital
        fields = ('name','location')