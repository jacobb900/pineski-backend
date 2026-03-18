from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pineski.views import PinViewSet

# Router automatycznie tworzy ścieżki dla Twoich pinesek (GET, POST itd.)
router = DefaultRouter()
router.register(r'pins', PinViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Wszystko pod adresem localhost:8000/api/pins/
]