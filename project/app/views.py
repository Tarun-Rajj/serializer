from django.http import Http404
from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        # print("rtr",serializer)
        # print("sds",serializer.data)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("aaa")
        serializer = TaskSerializer(data=request.data)
        print("qqqq",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_get = self.get_object(pk)
        serializer = TaskSerializer(task_get)
        return Response(serializer.data)
    
    def put(self, request, pk):
        task_get= self.get_object(pk)
        serializer = TaskSerializer(task_get, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        task_get = self.get_object(pk)
        task_get.delete()
        # return ({'msg':'Data deleted Successfully'})
        return Response(status=204)