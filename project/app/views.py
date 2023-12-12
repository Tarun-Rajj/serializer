from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Task
from .serializer import TaskSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskList(APIView):
    def get(self, request):
        try:
            tasks = Task.objects.all() # tasks contains a queryset which contain task object
            serializer = TaskSerializer(tasks, many=True)        
            return Response({"count": tasks.count(),"data":serializer.data})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Task Created Successfully","data":serializer.data}, status=201)
   
   
class TaskDetail(APIView):
    def get(self, request, pk):
        try:
            task_get = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(task_get)
            return Response({"msg":"Get particular Task","data":serializer.data})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def put(self, request, pk):
        task_get= get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task_get, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Updated Successfully","data":serializer.data})

    
    def delete(self, request, pk):
        try:
            task_get = get_object_or_404(Task, pk=pk)
            task_get.delete()
            return Response({"msg":"Task deleted Successfully"}, status = 201 )
        except Exception as e:
            return Response({"msg":"Error in deleting the Task","error": str(e)}, status=500)
   