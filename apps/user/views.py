"""
Views for the user API.
"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


@extend_schema_view(post=extend_schema(operation_id='회원 가입'))
class CreateUserView(generics.CreateAPIView):
    """Create new user in the system"""
    serializer_class = UserSerializer


@extend_schema_view(post=extend_schema(operation_id='로그인'))
class CreateTokenView(ObtainAuthToken):
    """Create a token for login."""
    serializer_class = AuthTokenSerializer


@extend_schema_view(
    get=extend_schema(operation_id='내 계정 정보'),
    put=extend_schema(operation_id='내 계정 정보 수정'),
    patch=extend_schema(operation_id='내 계정 정보 부분 수정'),
    delete=extend_schema(operation_id='내 계정 삭제')
)
class ManageSelfView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
