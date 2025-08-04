from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import FoodItem
def dashboard(request):
	today = timezone.localdate()
	foods = FoodItem.objects.filter(date=today)
	total = sum(f.calories for f in foods)
	return render(request, 'dashboard.html', {'food_items': foods, 'total_calories': total})


from django.db import transaction
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib import messages
from .models import FoodItem

@transaction.atomic
def add_food(request):
    """
    Create a new FoodItem from POST data and redirect to dashboard.
    Rejects empty/blank names, zero or negative calories.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Expected POST.")

    name = request.POST.get("name", "").strip()
    try:
        calories = int(request.POST.get("calories", 0))
    except ValueError:
        calories = 0

    if not name or calories <= 0:
        messages.error(request, "Please supply a valid food name and positive calories.")
        return redirect("dashboard")

    FoodItem.objects.create(name=name, calories=calories)
    messages.success(request, f"{name} added ({calories} kcal).")
    return redirect("dashboard")

def delete_food(request, pk):
    if request.method != "POST":
        return HttpResponseBadRequest("Expected POST.")

    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    messages.success(request, f"{food.name} removed.")
    return redirect("dashboard")
@transaction.atomic
def reset_day(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Expected POST.")

    today = timezone.localdate()
    deleted_count, _ = FoodItem.objects.filter(date=today).delete()
    if deleted_count:
        messages.success(request, f"Today’s log cleared ({deleted_count} items removed).")
    else:
        messages.info(request, "Nothing to reset—log was already empty.")
    return redirect("dashboard")
def add_food(request):
    if request.method == "POST":
        return redirect("dashboard")
    return render(request, "/addfood.html")