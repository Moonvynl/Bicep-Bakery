from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    path('', GeneralView.as_view(), name='general'),
]

app_name = 'shop'