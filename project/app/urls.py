from django.urls import path
from app import views

urlpatterns = [
    path('task/', views.TaskList.as_view()),
    path('task/<str:pk>/', views.TaskDetail.as_view())
]
