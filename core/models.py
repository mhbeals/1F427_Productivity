import enum

from django.db import models


class ChoicesEnum(enum.IntEnum):
    @classmethod
    def choices(cls):
        return tuple(((
            en.value,
            en.name.replace('_', ' ').title()
        ) for en in cls))


class Emoji(models.Model):
    emoji_code = models.CharField(max_length=50)

    def __str__(self):
        return self.emoji_code


class Unit(models.Model):
    unit_text = models.CharField(max_length=200)

    def __str__(self):
        return self.unit_text


@enum.unique
class TaskState(ChoicesEnum):
   NEW = 0
   CONTINUING = 1
   ENDED = 2


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    state = models.SmallIntegerField(choices=TaskState.choices(), blank=False, null=False)
    quantifier = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('task completed')
    user_id = models.IntegerField()

    def __str__(self):
        return self.task_text
    
