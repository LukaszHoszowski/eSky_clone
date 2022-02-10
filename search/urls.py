from django.urls import path, re_path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.Search.as_view(), name='search'),
    path('flights/', views.FlightsView.as_view(), name='flights'),
    path('flights/ajax/', views.ResultsAjaxView.as_view(), name='flights_ajax'),
]
