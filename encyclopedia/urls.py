from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = (
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry, name="entry"),
    url(r'^wiki/search/$', views.search, name="search")

        )
