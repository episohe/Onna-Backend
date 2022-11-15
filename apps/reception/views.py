from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics

from reception.models import Reception
from reception.serializers import ReceptionSerializer


@extend_schema_view(
    post=extend_schema(operation_id='매수장 생성'),
    get=extend_schema(operation_id='매수장 목록')
)
class ReceptionListCreateView(generics.ListCreateAPIView):
    queryset = Reception.objects.order_by('-id')
    serializer_class = ReceptionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
