from django.urls import include, path
from rest_framework import routers
from . import views
from django.shortcuts import redirect
from .views import CityFilterView
router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'capitals', views.CapitalViewSet)
router.register(r'cities', views.CityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),pip freeze > requirements.txt
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path(r'^favicon\.ico$', redirect().as_view(url='images/favicon.ico')),\
    path('filter/', CityFilterView.as_view(), name='filter'),
]