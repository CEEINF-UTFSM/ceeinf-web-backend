from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
