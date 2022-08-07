# Create your views here.
import jwt
from django.contrib.auth import authenticate
from ninja import Router

from user.schema import Message, Token

agency = Router(tags=['Agency'])


# 회원 가입 API

@agency.post("/login", response={200: Token, 400: Message, 401: Message})
def login(request, email: str, password: str):
    if not email or not password:
        return 400, {"message": "Bad Request"}
    account = authenticate(username=email, password=password)
    if account is not None:
        from django.conf import settings
        encoded_jwt = jwt.encode({"pk": account.pk}, settings.SECRET_KEY, algorithm="HS256")
        return 200, {"token": encoded_jwt, "id": account.pk}
    else:
        return 401, {"message": "Unauthorized"}


@agency.post("/logout", response={200: Message})
def logout(request):
    pass
