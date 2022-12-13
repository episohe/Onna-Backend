from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter

transaction_type_param = OpenApiParameter(
    name='transaction_type',
    description='거래 종류',
    type=OpenApiTypes.INT,
    location=OpenApiParameter.QUERY,
)

property_type_param = OpenApiParameter(
    name='property_type',
    description='부동산 종류',
    type=OpenApiTypes.INT,
    location=OpenApiParameter.QUERY,
)

region_param = OpenApiParameter(
    name='region',
    description='지역',
    type=OpenApiTypes.STR,
    location=OpenApiParameter.QUERY,
)

state_param = OpenApiParameter(
    name='state',
    description='거래 상태',
    type=OpenApiTypes.INT,
    location=OpenApiParameter.QUERY,
)