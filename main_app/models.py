from django.db import models

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=50)
    time = models.IntegerField(blank=True)
    person = models.CharField(max_length=10)

    def __str__(self):
        return f'Description: {self.description}, Time: {self.time}, Person: {self.person}'
