from django.urls import path
from .views import reverse, home

urlpatterns = [
    path('', home),
    path('check_sum', reverse)
]