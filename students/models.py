from django.db import models

# Create your models here.
class student(models.Model):
    roll_no=models.TextField()
    name=models.TextField(max_length=255)
    age=models.TextField()