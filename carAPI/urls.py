from django.urls import path
from .views import CarList, CarDetail, MakerList, MakerDetail, CarColorAPI

urlpatterns = [
    path('', CarList.as_view()),
    path('<int:pk>/', CarDetail.as_view()),
    path('<int:pk>/colors/', CarColorAPI.as_view()),
    path('makers/', MakerList.as_view()),
    path('makers/<int:pk>/', MakerDetail.as_view()),
]
