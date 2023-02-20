from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.
# contains most important data fields and behaviour

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','details']
# After making the models we need to migrate it 
