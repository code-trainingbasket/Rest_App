from django.shortcuts import render
from rest_framework.views import APIView
from .models import TaskModel
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TaskView(APIView):
    
    def get(self,request):
        obj = TaskModel.objects.all()
        serializer = TaskSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get(self,request,id=None):
        try:
            obj = TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        obj= TaskModel.objects.get(id=id)
        serializer = TaskSerializer(obj,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id=None):
        obj = TaskModel.objects.get(id=id)
        obj.delete()
        return Response(status = status.HTTP_410_GONE)