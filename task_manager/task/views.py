from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, views, generics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TaskListCreateAPIView(LoginRequiredMixin, generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(manager=self.request.user)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class TaskRetrieveUpdateDestroyView(
    LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(manager=self.request.user)
