from django.contrib import admin
from .models import HealthGoal, Food, Consume


@admin.register(HealthGoal)
class HealthGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'daily_calorie_goal', 'carb_goal', 'protein_goal', 'fat_goal')
    search_fields = ('user__username',)
    list_filter = ('daily_calorie_goal',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'carbs', 'proteins', 'fats', 'calories')
    search_fields = ('name',)
    list_filter = ('calories',)


@admin.register(Consume)
class ConsumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_consumed', 'date')
    search_fields = ('user__username', 'food_consumed__name')
    list_filter = ('date', 'food_consumed')
