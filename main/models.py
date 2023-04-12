from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    name = models.CharField(max_length=100, null= True)
    createdAt = models.DateTimeField(auto_now_add=True, null= True, blank= True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class TodoItems(models.Model):
    name = models.TextField(max_length=100, null= True)
    description = models.TextField(max_length=200, null= True, blank= True)
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, null= True, blank= True)
    todo = models.ForeignKey(Todo, null= True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name

