from django.contrib import admin
from django.urls import path, include
from app.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("api/", api.urls),
]
