from rest_framework import viewsets, generics

from .pagination import StandardResultsSetPagination
from .serializers import CitySerializer
from .models import City
from .serializers import CountrySerializer
from .models import Country
from .serializers import CapitalSerializer
from .models import Capital
from .models import Country
from urllib.parse import unquote

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer


class CapitalViewSet(viewsets.ModelViewSet):
    queryset = Capital.objects.all().order_by('name')
    serializer_class = CapitalSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer


class CitiesByCountryList(generics.ListAPIView):
    serializer_class = CitySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        country_name_encoded = self.kwargs['name']
        country_name = unquote(country_name_encoded)
        return City.objects.filter(country__name=country_name).order_by('name')

from django.contrib.gis.geos import Polygon
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City

class CityFilterView(APIView):
    def get(self, request):
        bbox = request.GET.get('bbox')
        if bbox:
            bbox_list = bbox.split(',')
            polygon = Polygon.from_bbox(bbox_list)
            cities = City.objects.filter(location__within=polygon)
            city_names = [city.name for city in cities]
            return Response({'cities': city_names})
        else:
            return Response({'error': 'bbox parameter is missing'})

