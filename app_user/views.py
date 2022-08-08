
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_user.serializers import *


@api_view(['POST'])
def AppUserView(request):
    if request.method == 'POST':
        pass

    else:
        pass

