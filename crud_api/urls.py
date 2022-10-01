from django.urls import path
from . views import *

app_name = 'crud_api'

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', Details.as_view()),
    path('create/', CreateToDo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view())
]
