from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if len(self.title) > 100:
            raise ValidationError("Title cannot be longer than 100 characters")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
