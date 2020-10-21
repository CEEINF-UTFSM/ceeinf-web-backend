from django.urls import path

from .views import ConvalidationsView


urlpatterns = [
    path("convalidaciones",  ConvalidationsView.as_view())
]