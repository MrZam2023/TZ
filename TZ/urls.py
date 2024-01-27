from TZDjango.views import Task_List, Task_Detail
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', Task_List.as_view()),
    path('tasks/<int:pk>/', Task_Detail.as_view()),
]
