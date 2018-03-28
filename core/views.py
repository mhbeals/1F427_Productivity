import random

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView

from core import forms, models


class TaskSubmitView(CreateView):
    model = models.Task
    template_name = 'core/index.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('core:index')

    def get_initial(self):
        """
        Add default user_id - users are not yet implemented.
        """
        initial = super().get_initial()

        initial['user_id'] = 1

        return initial

    def form_valid(self, form):
        """
        Add missing fields for DB.
        """

        # Timestamp cannot be from form.initial since we want it to be set when the Task is created
        form.instance.timestamp = timezone.datetime.now()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Add data to the template context.

        - emoji_options: list of emoji to offer to user
        - morning: Dictionary of tasks in the morning
            - happy: Tasks with a 'happy' emoji
            - not_so_happy: Tasks with a 'not so happy' emoji
            - working_thinking: Tasks with a 'working/thinking' emoji
            - fun: Tasks with a 'fun' emoji
        - afternoon: See morning
        - night: See morning
        """
        context = super().get_context_data(**kwargs)

        context['emoji_options'] = self.get_random_emoji()

        queryset_morning = models.Task.objects.filter(timestamp__hour__range=(4, 11))
        context['morning'] = {
            'happy': queryset_morning.filter(emoji__group=models.EmojiGroup.HAPPY),
            'not_so_happy': queryset_morning.filter(emoji__group=models.EmojiGroup.NOTSOHAPPY),
            'working_thinking': queryset_morning.filter(emoji__group=models.EmojiGroup.WORKINGTHINKING),
            'fun': queryset_morning.filter(emoji__group=models.EmojiGroup.FUN),
        }

        queryset_afternoon = models.Task.objects.filter(timestamp__hour__range=(12, 18))
        context['afternoon'] = {
            'happy': queryset_afternoon.filter(emoji__group=models.EmojiGroup.HAPPY),
            'not_so_happy': queryset_afternoon.filter(emoji__group=models.EmojiGroup.NOTSOHAPPY),
            'working_thinking': queryset_afternoon.filter(emoji__group=models.EmojiGroup.WORKINGTHINKING),
            'fun': queryset_afternoon.filter(emoji__group=models.EmojiGroup.FUN),
        }

        queryset_night = models.Task.objects.filter(timestamp__hour__range=(19, 23)).union(
            models.Task.objects.filter(timestamp__hour__range=(0, 3))
        )
        context['night'] = {
            'happy': queryset_night.filter(emoji__group=models.EmojiGroup.HAPPY),
            'not_so_happy': queryset_night.filter(emoji__group=models.EmojiGroup.NOTSOHAPPY),
            'working_thinking': queryset_night.filter(emoji__group=models.EmojiGroup.WORKINGTHINKING),
            'fun': queryset_night.filter(emoji__group=models.EmojiGroup.FUN),
        }

        return context

    @classmethod
    def get_random_emoji(cls):
        """Get a list of random emoji (as models.Emoji instance),

        The number from each required group is set (2 happy, 1
        notsohappy, 2 workingthinking, 1 fun). The ordering of the list
        is predictable.

        :return: List of models.Emoji
        """
        random_emoji = []

        for group, n_emoji in (
                (models.EmojiGroup.HAPPY, 2),
                (models.EmojiGroup.NOTSOHAPPY, 1),
                (models.EmojiGroup.WORKINGTHINKING, 2),
                (models.EmojiGroup.FUN, 1)):
            matching_emoji = list(models.Emoji.objects.filter(group=group))
            for entry in random.sample(matching_emoji, n_emoji):
                random_emoji.append(entry)

        sorted_random_emoji = sorted(random_emoji, key=(lambda x: x.pk))

        return sorted_random_emoji
