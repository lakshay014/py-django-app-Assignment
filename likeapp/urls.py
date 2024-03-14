from django import urls
from django.urls import path
from . import views

#url Configurations
urlpatterns = [
    path("",views.main_page),
    path("addEvent/",views.add_new),
    path("like/",views.like_event)
]