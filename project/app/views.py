from django.http import Http404
from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all() # tasks contains a queryset which contain task object
        serializer = TaskSerializer(tasks, many=True)        
        return Response({"count": len(serializer.data),"data":serializer.data})
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Task Created Successfully","data":serializer.data}, status=201)
        return Response(serializer.errors, status=400)
    
class TaskDetail(APIView):

    def get_object_or_404(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_get = self.get_object_or_404(pk)
        serializer = TaskSerializer(task_get)
        return Response({"msg":"Get particular Task","data":serializer.data})
    
    def put(self, request, pk):
        try:
            task_get= self.get_object_or_404(pk)
            serializer = TaskSerializer(task_get, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Updated Successfully","data":serializer.data})
            else:
                return Response(serializer.error, status=400)
        except Http404:
            return Response({"Error":"Object not found"},status=404)
        except Exception as e:
            return Response({"msg": "An error occured", "error": str(e)}, status=500) 
    
    def delete(self, request, pk):
        task_get = self.get_object_or_404(pk)
        task_get.delete()
        return Response({"msg":"Task deleted Successfully"}, status = 201 )