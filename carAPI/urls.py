from django.urls import path
from .views import CarList, CarDetail, MakerList, MakerDetail, CarColorAPI


urlpatterns = [
    path(r'', CarList.as_view()),
    path(r'<int:pk>/', CarDetail.as_view()),
    path(r'<int:pk>/colors', CarColorAPI.as_view()),
    path(r'makers/', MakerList.as_view()),
    path(r'makers/<int:pk>/', MakerDetail.as_view()),
]
