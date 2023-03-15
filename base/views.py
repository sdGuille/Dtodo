from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
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


class TaskCreate(CreateView):
    model = Task
    template_name = "task_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks")