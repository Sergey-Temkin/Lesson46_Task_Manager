from django.db import models
from django.contrib.auth.models import User                   # Import the User model

class Task(models.Model):
    name = models.CharField(max_length=255)                   # Task name
    deadline = models.DateField()                             # Task deadline date
    done = models.BooleanField(default=False)                 # Done status (True/False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    
    def __str__(self):
        return self.name