
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api_app.urls')),
    path('',include('class_based_app.urls')),
]
