from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Task
from .serializer import TaskSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def Task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        print(tasks)
        serializer = TaskSerializer(tasks,many=True)
        return Response({"msg":"Get all Tasks","data":serializer.data})
    elif request.method=="POST":
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Task Created Successfully","data": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def Task_detail(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer = TaskSerializer(task,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"msg": "Updated data Successfully","data":serializer.data},status=status.HTTP_202_ACCEPTED)
        elif request.method == 'DELETE':
            task.delete()
            return Response({"msg":"Task Delete Successfully"},status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"error":str(e)})
    