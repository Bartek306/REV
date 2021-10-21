from django.urls import path
from .views import check_sum, home

urlpatterns = [
    path('', home),
    path('check_sum', check_sum)
]