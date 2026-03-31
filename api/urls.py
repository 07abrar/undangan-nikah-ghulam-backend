from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("couple/", views.couple),
    path("event/", views.event),
]
