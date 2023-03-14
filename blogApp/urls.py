from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name='hello'),
    path("greet/", views.greet, name='greet'),
    path("simi/", views.simi, name='simi'),
    path("", views.home, name='home'),
]
