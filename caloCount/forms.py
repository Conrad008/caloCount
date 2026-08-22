from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter a Food item...',
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'Please specify the calories ',
                'min': '1',
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
        }