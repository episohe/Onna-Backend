from rest_framework import generics

from reception.models import Reception
from reception.serializers import ReceptionSerializer


# Create your views here.
class ReceptionListCreateView(generics.ListCreateAPIView):
    queryset = Reception.objects.order_by('-id')
    serializer_class = ReceptionSerializer


class ReceptionManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reception.objects.order_by('-id')
    serializer_class = ReceptionSerializer
    lookup_url_kwarg = "pk"
