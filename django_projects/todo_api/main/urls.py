from django.urls import path
from . import views

urlpatterns = [
    # class urls
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view())

    # function urls
    # path('tasks/', views.tasks_list_create_view),
    # path('tasks/<int:pk>/', views.task_detail_view),


    # path('tasks/', views.tasks_list),  # id не нужно Get
    # path('tasks/<int:pk>/', views.task_detail), # id нужно Get
    # path('tasks-create/', views.task_create), # id не нужно
    # path('tasks-update/<int:pk>/', views.task_update), # id нужно PUT/Patch
    # path('tasks-delete/<int:pk>/', views.task_delete), # id нужно DELETE


]
# api/v1/books/ GET-LIST POST create
# api/v1/books/<id>/ GET - detail PUT/PATCH - update DELETE - delete