from django.core.exceptions import ValidationError
from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.params import transaction_type_param, property_type_param, region_param
from reception.models import Reception
from reception.serializers import ReceptionSerializer


@extend_schema_view(
    post=extend_schema(operation_id='매수장 생성'),
)
class ReceptionCreateView(generics.CreateAPIView):
    queryset = Reception.objects.order_by('-id')
    serializer_class = ReceptionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReceptionListView(APIView):
    """Search"""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        operation_id="매수장 조회",
        responses=ReceptionSerializer,
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
            reception = Reception.objects.filter(q).select_related('user').order_by('-created')

        except ValidationError:
            reception = Reception.objects.all().order_by('-created')

        serializer = ReceptionSerializer(reception, many=True)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(operation_id="매수장 상세 보기"),
    put=extend_schema(operation_id="매수장 수정", deprecated=True),
    patch=extend_schema(operation_id="매수장 부분 수정"),
    delete=extend_schema(operation_id="매수장 삭제")
)
class ReceptionManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reception.objects.order_by('-id')
    serializer_class = ReceptionSerializer
    lookup_url_kwarg = "pk"
