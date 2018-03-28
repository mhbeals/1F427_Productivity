from django.forms.models import HiddenInput
from django.forms.models import ModelForm

from easy_select2 import widgets as select2

from core.models import Emoji, Task


class TaskForm(ModelForm):
    """
    Form used to create instances of Task
    """

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'state': HiddenInput,
            'units': select2.Select2,
            'emoji': HiddenInput,
        }
