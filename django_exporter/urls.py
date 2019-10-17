# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_exporter'
urlpatterns = [
    url(
        regex="^Reusable django app to export large datasets./~create/$",
        view=views.Reusable django app to export large datasets.CreateView.as_view(),
        name='Reusable django app to export large datasets._create',
    ),
    url(
        regex="^Reusable django app to export large datasets./(?P<pk>\d+)/~delete/$",
        view=views.Reusable django app to export large datasets.DeleteView.as_view(),
        name='Reusable django app to export large datasets._delete',
    ),
    url(
        regex="^Reusable django app to export large datasets./(?P<pk>\d+)/$",
        view=views.Reusable django app to export large datasets.DetailView.as_view(),
        name='Reusable django app to export large datasets._detail',
    ),
    url(
        regex="^Reusable django app to export large datasets./(?P<pk>\d+)/~update/$",
        view=views.Reusable django app to export large datasets.UpdateView.as_view(),
        name='Reusable django app to export large datasets._update',
    ),
    url(
        regex="^Reusable django app to export large datasets./$",
        view=views.Reusable django app to export large datasets.ListView.as_view(),
        name='Reusable django app to export large datasets._list',
    ),
	]
