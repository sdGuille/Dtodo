from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Task


class TaskList(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    paginate_by = 5
    ordering = ["-complete"]


class TaskDetail(DetailView):
    model = Task
    template_name = "task.html"
    context_object_name = "task"
