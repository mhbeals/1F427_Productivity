from django.views.generic.edit import CreateView

from core import forms, models


class TaskSubmitView(CreateView):
    model = models.Task
    template_name = 'core/index.html'
    form_class = forms.TaskForm
