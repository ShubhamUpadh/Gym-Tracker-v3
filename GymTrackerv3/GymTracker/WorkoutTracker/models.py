from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 20)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username + self.phone

class predefined_exercises(models.Model):
    
    class ExerciseType(models.TextChoices):
        ISOLATION = 'isolation', _('ISOLATION EXERCISE')
        COMPOUND = 'compound', _('COMPOUND EXERCISE')
    id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length= 50)
    major_muscle = models.CharField(max_length=20)
    exercise_type = models.CharField(max_length = 10, choices = ExerciseType.choices)
