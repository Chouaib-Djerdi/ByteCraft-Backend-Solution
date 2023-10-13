from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskListCreateAPIView.as_view(), name="task-list-create"),
    path(
        "tasks/<int:pk>/",
        views.TaskRetrieveUpdateDestroyView.as_view(),
        name="task-retrieve-update-destroy",
    ),
]
