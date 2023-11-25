from django import forms
from .models import item

INPUT_CLASSES ='w-fill py-4 px-6 rounded-xl border'

class EditItemForm(forms.ModelForm):
    class Meta:
        model= item
        fields = ( 'name', 'description','price', 'image','is_sold',)
   
        widgets = {
          
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class NewItemForm(forms.ModelForm):
    class Meta:
        model= item
        fields = ('category', 'name', 'description','price', 'image',)
   
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }