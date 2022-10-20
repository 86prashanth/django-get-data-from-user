from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('result',result,name='result'),
    # path('sum',sum,name='sum'),
]
