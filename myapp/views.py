from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import FoodItem  # Make sure this import is correct for your project structure


def dashboard(request):
    today = timezone.localdate()
    foods = FoodItem.objects.filter(date=today)
    total = sum(f.calories for f in foods)
    return render(request, "tracker/dashboard.html", 
                {"foods": foods, "total": total})


def add_food(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        try:
            calories = int(request.POST.get("calories", 0))
        except ValueError:
            calories = 0

        if name and calories > 0:
            FoodItem.objects.create(name=name, calories=calories)
            messages.success(request, f"{name} added.")
            return redirect("dashboard")

    return redirect("dashboard")


def delete_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    messages.success(request, f"{food.name} removed.")
    return redirect("dashboard")


def reset_day(request):
    today = timezone.localdate()
    FoodItem.objects.filter(date=today).delete()
    messages.success(request, "Today's log cleared.")
    return redirect("dashboard")