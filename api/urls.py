from django.urls import include, path

from api import views

urlpatterns = [
    path("difference", views.difference, name="difference"),
]
