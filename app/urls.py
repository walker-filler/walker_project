from django.urls import path
from app.views import product_list

urlpatterns = [
    path("", product_list),
]
