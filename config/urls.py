from django.contrib import admin
from django.urls import path, include
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('auth/users/', UserViewSet.as_view({'post': 'create'}),
         name='user-create'),
    path('api/', include('tickets.urls')),
]
