from django.urls import path
from .views import Image

urlpatterns = [
    path(r'image/', Image.as_view())
]