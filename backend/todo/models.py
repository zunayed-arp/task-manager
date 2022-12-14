from django.db import models




class Todo(models.Model):
    title = models.CharField(max_length=120)
    description= models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.title
    
    
