from django.urls import include, path
from rest_framework import routers
from . import views

from .views import CityFilterView, CitiesByCountryList

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'capitals', views.CapitalViewSet)
router.register(r'cities', views.CityViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'^favicon\.ico$', redirect().as_view(url='images/favicon.ico')),
    path('filter/', CityFilterView.as_view(), name='filter'),
    path('countries/<str:name>/cities/', CitiesByCountryList.as_view(), name='cities-by-country'),


]