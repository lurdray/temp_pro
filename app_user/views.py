from app_user.models import *

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_user.serializers import *




@api_view(['POST'])
def RegisterView(request):
    if request.method == 'POST':

        request.session.create()
        auth_code = request.session.session_key

        first_name =request.data["first_name"]
        last_name =request.data["last_name"]
        email =request.data["email"]
        password = request.data["password"]



        try:

            user = User(username=email, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()

            app_user = AppUser.objects.create(user=user, first_name=first_name, last_name=last_name, auth_code=auth_code)
            app_user.save()

            data = {"detail": "Successful registration", "status_lean": True}

            serializer = StatusLeanSerializer(data=data)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        except:

            data = {"detail": "Error!!", "status_lean": False}

            serializer = StatusLeanSerializer(data=data)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


