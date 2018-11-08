from django.urls import path

from fastfoodrq.ordering import views

urlpatterns = [
    path('', views.index, name='index'),
]
