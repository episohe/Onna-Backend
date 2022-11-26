"""URL mappings for the reception API."""
from django.urls import path

from reception import views

app_name = 'reception'

urlpatterns = [
    path('notes/', views.ReceptionCreateView.as_view(), name='receptions'),
    path('notes/search/', views.ReceptionListView.as_view(), name='reception-list'),
    path('note/<int:pk>/', views.ReceptionManageView.as_view(), name='reception'),
]
