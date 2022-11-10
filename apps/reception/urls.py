"""URL mappings for the reception API."""
from django.urls import path

from reception import views

app_name = 'reception'

urlpatterns = [
    path('receptions', views.ReceptionListCreateView.as_view(), name='receptions'),
    path('reception', views.ReceptionManageView.as_view(), name='reception'),
]
