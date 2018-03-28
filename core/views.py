from django.views.generic.edit import CreateView

from core import forms, models


class TaskSubmitView(CreateView):
    model = models.Task
    template_name = 'core/index.html'
    form_class = forms.TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['emoji_options'] = self.get_random_emoji()

        return context

    @classmethod
    def get_random_emoji(cls):
        """
        Get a list of random emoji (as models.Emoji instance), making sure there are enough from each required group.

        :return: List of emoji
        """
        emoji = []

        return emoji
