from django.urls import include, path
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'registerdusers', views.RegisteredUserList, basename='registerdusers')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/registration/', Registration.as_view(), name='api-registration'),
    
]