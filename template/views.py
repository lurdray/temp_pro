
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from template.serializers import *


@api_view(['POST'])
def TemplateView(request):
    if request.method == 'POST':
        pass

    else:
        pass

