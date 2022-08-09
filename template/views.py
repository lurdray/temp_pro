from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.http import HttpResponse

from template.serializers import *
from template.models import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddTemplateView(request):
    if request.method == 'POST':

        app_user = AppUser.objects.get(id=1)

        template_name = request.data["template_name"]
        subject = request.data["subject"]
        body = request.data["body"]

        template = Template.objects.create(app_user=app_user, template_name=template_name, subject=subject, body=body)
        template.save()

        data = {
            "status_lean": True,
            "detail": "Successful",

        }

        serializer = StatusLeanSerializer(data=data)

        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    else:

        data = {
        "status_lean": False,
        "detail": "Not Successful",

        }

        serializer = StatusLeanSerializer(data=data)

        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllTemplateView(request):
    if request.method == 'GET':
        templates = Template.objects.all().order_by("-pub_date")

        serializer = TemplateSerializer(templates, many=True)
        if serializer:
            return Response(serializer.data)

        else:
            return HttpResponse(str("errors!"))



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetTemplateView(request, template_id):
    if request.method == 'GET':
        template = Template.objects.get(id=template_id)

        serializer = TemplateSerializer(template)
        if serializer:
            return Response(serializer.data)

        else:
            return HttpResponse(str("errors!"))




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateTemplateView(request, template_id):
    if request.method == 'PUT':
        template_name = request.data["template_name"]
        subject = request.data["subject"]
        body = request.data["body"]

        template = Template.objects.get(id=template_id)
        template.template_name = template_name
        template.subject = subject
        template.body = body
        template.save()

        data = {
            "status_lean": True,
            "detail": "Successful",

        }

        serializer = StatusLeanSerializer(data=data)

        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteTemplateView(request, template_id):
    if request.method == 'DELETE':

        template = Template.objects.get(id=template_id)
        template.status = False
        template.save()

        data = {
            "status_lean": True,
            "detail": "Successful",

        }

        serializer = StatusLeanSerializer(data=data)

        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

