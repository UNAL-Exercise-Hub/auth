from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.hashers import make_password
from AuthenticationApp.models import Login
import environ
import datetime
import jwt
env = environ.Env()
environ.Env.read_env()


@api_view(["POST"])
def login(request: Request):
    email = request.data["email"]
    password = request.data["password"]

    try:
        user = Login.objects.get(UserEmail= email)

        if(user.UserPasswordHash == make_password(password, salt=env("SALT_JWT"))):
            token = jwt.encode(payload={"email": email, "exp": datetime.datetime.now()+datetime.timedelta(days=1)}, key=env("SECRET_JWT"), algorithm="HS256")
            return Response({"token": token})
        else:
            return Response({"error": "Credenciales incorrectas"})
    except:
        return Response({"error": "Credenciales incorrectas"})


@api_view(["GET"])
def whoAmI(request: Request):
    token = request.data["token"]

    try:
        decode = jwt.decode(jwt=token,key= env("SECRET_JWT"),algorithms=["HS256"])
    except:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response({"email": decode["email"]})