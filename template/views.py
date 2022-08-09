from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.http import HttpResponse

from template.serializers import *
from template.models import *

from rest_framework_simplejwt.backends import TokenBackend

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddTemplateView(request):
    if request.method == 'POST':

        app_user = AppUser.objects.get(user__username=request.user)

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
        try:
            templates = Template.objects.filter(app_user__user=request.user).order_by("-pub_date")

            serializer = TemplateSerializer(templates, many=True)
            if serializer:
                return Response(serializer.data)

            else:
                return HttpResponse(str("errors!"))

        except:
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
def GetTemplateView(request, template_id):
    if request.method == 'GET':

        try:
            template = Template.objects.get(id=template_id, app_user__user=request.user)

            serializer = TemplateSerializer(template)
            if serializer:
                return Response(serializer.data)

            else:
                return HttpResponse(str("errors!"))

        except:
            data = {
            "status_lean": False,
            "detail": "Not Successful",

            }

            serializer = StatusLeanSerializer(data=data)

            if serializer.is_valid():
                #serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateTemplateView(request, template_id):
    if request.method == 'PUT':
        try:
            template_name = request.data["template_name"]
            subject = request.data["subject"]
            body = request.data["body"]

            template = Template.objects.get(id=template_id, app_user__user=request.user)
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

        except:
            data = {
            "status_lean": False,
            "detail": "Not Successful",

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

        try:
            template = Template.objects.get(id=template_id, app_user__user=request.user)
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

        except:
            data = {
            "status_lean": False,
            "detail": "Not Successful",

            }

            serializer = StatusLeanSerializer(data=data)

            if serializer.is_valid():
                #serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

