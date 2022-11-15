from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics

from realty.models import Realty
from realty.serializers import RealtySerializer


@extend_schema_view(
    post=extend_schema(operation_id='매물장 생성'),
    get=extend_schema(operation_id='매물장 목록')
)
class RealtyListCreateView(generics.ListCreateAPIView):
    queryset = Realty.objects.order_by('-id')
    serializer_class = RealtySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
