from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class HealthGoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_calorie_goal = models.IntegerField(default=2000)
    carb_goal = models.FloatField(default=50)
    protein_goal = models.FloatField(default=50)
    fat_goal = models.FloatField(default=50)

    def __str__(self):
        return f"{self.user.username}'s Health Goal"


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.name


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} consumed {self.food_consumed.name} on {self.date}"
