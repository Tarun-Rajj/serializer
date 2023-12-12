from django.urls import path
from task import views

urlpatterns = [
    path('task/', views.Task_list),
    path('add-task/<str:pk>/',views.Task_detail),
   
]
