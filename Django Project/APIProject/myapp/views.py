from django.shortcuts import render
from .models import studInfo
from .serializers import StudSerial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def getdata(request):
    if request.method=="GET":
        stdata=studInfo.objects.all()
        serial=StudSerial(stdata,many=True)
        return Response(serial.data)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studInfo.objects.get(id=id)
    except studInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=StudSerial(stid)
    return Response(serial.data,status=status.HTTP_200_OK)
    
