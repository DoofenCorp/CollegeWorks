from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('add', views.add, name='Add'),
    path('sub', views.sub, name='Subtract'),
    path('multiply', views.multiply, name='Multiply'),
    path('divide', views.divide, name='Divide')
]

