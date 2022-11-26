from django.core.exceptions import ValidationError
from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from core.params import *
from realty.models import Realty
from realty.serializers import RealtySerializer


@extend_schema_view(
    post=extend_schema(operation_id='매물장 생성'),
)
class RealtyCreateView(generics.CreateAPIView):
    queryset = Realty.objects.order_by('-id')
    serializer_class = RealtySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RealtyListView(APIView):
    """Search"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        operation_id="매물장 조회",
        responses=RealtySerializer,
        parameters=[transaction_type_param, property_type_param, region_param]
    )
    def get(self, request):

        q = Q()
        if transaction_type := request.GET.get("transaction_type"):
            q &= (Q(transaction_type=transaction_type))
        if property_type := request.GET.get('property_type', None):
            q &= (Q(property_type=property_type))
        if region := request.GET.get('region', None):
            q &= (Q(region__contains=region))

        try:
            reception = Realty.objects.filter(q).select_related('user').order_by('-created')

        except ValidationError:
            reception = Realty.objects.all().order_by('-created')

        serializer = RealtySerializer(reception, many=True)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(operation_id="매물장 상세 보기"),
    put=extend_schema(operation_id="매물장 수정", deprecated=True),
    patch=extend_schema(operation_id="매물장 부분 수정"),
    delete=extend_schema(operation_id="매물장 삭제")
)
class RealtyManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Realty.objects.order_by('-id')
    serializer_class = RealtySerializer
    lookup_url_kwarg = "pk"
