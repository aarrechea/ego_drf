#Imports
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_ego import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



# Patterns
urlpatterns = [    
    path('admin/', admin.site.urls),    
    path("api/", include(("apps.router", "apps"), namespace="apps-api")),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Optional UI for spectacular:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]



# Media files
if settings.DEBUG and not settings.USE_S3:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)