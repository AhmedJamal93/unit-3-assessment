from django.forms import ModelForm
from .models import Task

class TaskList(ModelForm):
    class Meta:
        model = Task
        fields = ['description','time','person']
