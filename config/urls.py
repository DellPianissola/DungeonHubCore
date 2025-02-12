from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView

from config import settings
from core.token.api.views import LoginView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/dharma/', include('dharma.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
