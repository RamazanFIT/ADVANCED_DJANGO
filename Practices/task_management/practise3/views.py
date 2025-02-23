from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import HealthGoalForm
from .models import Consume, HealthGoal


@login_required
def nutrient_data(request):
    consumed = Consume.objects.filter(user=request.user)
    goals = HealthGoal.objects.get(user=request.user)

    data = {
        "carbs": sum(c.food_consumed.carbs for c in consumed),
        "proteins": sum(c.food_consumed.proteins for c in consumed),
        "fats": sum(c.food_consumed.fats for c in consumed),
        "calories": sum(c.food_consumed.calories for c in consumed),
        "goals": {
            "carbs": goals.carb_goal,
            "proteins": goals.protein_goal,
            "fats": goals.fat_goal,
            "calories": goals.daily_calorie_goal
        }
    }

    return JsonResponse(data)


@login_required
def set_goals(request):
    goal, created = HealthGoal.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = HealthGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = HealthGoalForm(instance=goal)

    return render(request, "practise3/set_goals.html", {"form": form})


def index(request):
    health_goal = HealthGoal.objects.get(user=request.user)
    return render(request, "practise3/index.html", {"health_goal": health_goal})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "practise3/register.html", {"form": form})


@login_required
def chart_data(request):
    consumed = Consume.objects.filter(user=request.user)

    data = {
        "labels": [c.food_consumed.name for c in consumed],
        "carbs": [c.food_consumed.carbs for c in consumed],
        "proteins": [c.food_consumed.proteins for c in consumed],
        "fats": [c.food_consumed.fats for c in consumed],
        "calories": [c.food_consumed.calories for c in consumed],
    }

    return JsonResponse(data)
