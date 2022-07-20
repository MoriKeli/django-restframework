from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('article/', include('api.api_urls')),
    path('admin/', admin.site.urls),
]
