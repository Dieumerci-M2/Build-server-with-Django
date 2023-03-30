from django.urls import path
from . import views

urlpatterns = [
    path("render", views.index, name="index"),
    path("md/", views.md, name="md"),
    path("<str:name>", views.greet, name="greet") 
]