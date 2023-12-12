from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    


