from django.urls import path

from .views import ConvalidationsView, SubjectsView, news_view


urlpatterns = [
    path("convalidaciones",  ConvalidationsView.as_view()),
    path("ramos-y-ayudantias", SubjectsView.as_view()),
    path("noticias", news_view),
]
