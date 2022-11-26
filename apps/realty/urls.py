"""URL mappings for the reception API."""
from django.urls import path

from realty import views

app_name = 'realty'

urlpatterns = [
    path('notes/', views.RealtyCreateView.as_view(), name='realty'),
    path('notes/search/', views.RealtyListView.as_view(), name='realty-search'),
    path('note/<int:pk>/', views.RealtyManageView.as_view(), name='realty-manage'),
]
