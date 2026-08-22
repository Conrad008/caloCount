from django.shortcuts import render , redirect, get_object_or_404

from django.db.models import Sum
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    food_items = FoodItem.objects.all()
    total_calories = food_items.aggregate(Sum('calories'))['calories__sum'] or 0
    form = FoodItemForm()

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'calorie_tracker/index.html', {
        'food_items': food_items,
        'total_calories': total_calories,
        'form': form,
    })

def delete_food(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('index')