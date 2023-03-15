from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.
from .models import Task


class CustomLoginView(LoginView):
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")
    

class RegisterPage(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    # paginate_by = 5
    # ordering = ["complete"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context['tasks'].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task.html"
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_form.html"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_form.html"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("tasks")