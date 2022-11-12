"""URL mappings for the reception API."""
from django.urls import path

from realty import views

app_name = 'realty'

urlpatterns = [
    path('notes', views.RealtyListCreateView.as_view(), name='realty'),
    path('note/<int:pk>', views.RealtyManageView.as_view(), name='realty-manage'),
]

# todo 매물장/매수장 url 다시 생각해보기.
