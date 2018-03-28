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
        exclude = ['timestamp']
        widgets = {
            'state': HiddenInput,       # Will be set by Javascript on frontend
            'units': select2.Select2,   # Select from options list
            'emoji': HiddenInput,       # Will be set by Javascript on frontend
            'user_id': HiddenInput,     # Uses default value
        }
