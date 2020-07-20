from django.urls import path
from .views import homepage

# base App urls

urlpatterns = [
    path('', homepage, name='homepage'),
]

