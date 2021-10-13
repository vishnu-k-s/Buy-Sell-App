
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

#Documentation using swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


   
urlpatterns = [
    path('admin/', admin.site.urls),

    #Including urls from buy_sell app
    path('', include('buy_sell.urls')),
    path('', include('mainapp.urls')),
    #path('', include('chat.urls')),
    path('', include('notifications_app.urls')),
    path('', include('rest_api.urls')),

    #For documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentation/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#For serving uploaded files
