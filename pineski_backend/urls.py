from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pineski.views import PinViewSet
# IMPORTY DO LOGOWANIA:
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'pins', PinViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # ŚCIEŻKI DO LOGOWANIA (Tędy WebStorm wyśle hasło):
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]