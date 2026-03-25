from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pineski.views import PinViewSet
# --- DODANE IMPORTY DLA ZDJĘĆ ---
from django.conf import settings
from django.conf.urls.static import static
# -------------------------------

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
    # ŚCIEŻKI DO LOGOWANIA:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# --- DOKLEJKA OBSŁUGUJĄCA WYŚWIETLANIE ZDJĘĆ ---
# To sprawia, że pod adresem http://localhost:8000/media/ zobaczysz wgrane fotki
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)