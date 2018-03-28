from django.views.generic.edit import CreateView

from core import forms, models


class TaskSubmitView(CreateView):
    model = models.Task
    template_name = 'core/index.html'
    form_class = forms.TaskForm

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
        """
        Get a list of random emoji (as models.Emoji instance), making sure there are enough from each required group.

        :return: List of emoji
        """
        emoji = []

        return emoji
