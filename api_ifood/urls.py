
from django.contrib import admin
from django.urls import path
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', api.urls),
]
