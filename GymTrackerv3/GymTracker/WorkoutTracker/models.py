from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class users(models.Model): # users model defined
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 20)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username + " | " + self.phone

class predefined_exercises(models.Model):   # predefined exercises
    
    class ExerciseType(models.TextChoices):
        ISOLATION = 'isolation', _('ISOLATION EXERCISE')
        COMPOUND = 'compound', _('COMPOUND EXERCISE')
    id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length= 50)
    major_muscle = models.CharField(max_length=20)
    exercise_type = models.CharField(max_length = 10, choices = ExerciseType.choices)

    def __str__(self):
        return self.exercise_name + " | " + self.major_muscle

class date_workout(models.Model):
    id = models.AutoField(primary_key=True)
    exercise_id = models.ForeignKey(predefined_exercises,on_delete =models.CASCADE,related_name = 'date_of_exercise')   # use this to access the date on which an exercise was done
    user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name = 'exercise_dates_of_user')
    workout_date = models.DateField()

    def __str__(self):
        return self.exercise_id + " | " + self.user_id + " | " + self.workout_date

class set_details(models.Model):
    id = models.AutoField(primary_key=True)
    date_workout_id = models.ForeignKey(date_workout, on_delete=models.CASCADE, related_name = 'undecided')
    set_number = models.IntegerField()
    weight = models.CharField(max_length = 20)
    repitition = models.CharField(max_length = 20)
    remarks = models.CharField(max_length=50)

    def __str__(self):
        return self.date_workout_id + " | " + self.weight + " | " + self.repitition
    


