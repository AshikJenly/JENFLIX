from django.urls import path

from .views import Movie_Page_view

urlpatterns = [path("", Movie_Page_view),]
