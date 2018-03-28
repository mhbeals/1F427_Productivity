from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    state = models.IntegerField(default=1)
    quantifier = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('task completed')
    user_id = models.IntegerField()
    def __str__(self):
        return self.task_text
    
class Emoji(models.Model):
    emoji_code = models.CharField(max_length=5)    
    def __str__(self):
        return self.emoji_code

class Unit(models.Model):
    unit_text = models.CharField(max_length=200)
    def __str__(self):
        return self.unit_text
