from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=12, default='Note')
    text = models.TextField(default='Help my mom')
    priority = models.CharField(max_length=9)
    task_class = models.CharField(max_length=10)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    
    
    class Meta:
        db_table = 'note'