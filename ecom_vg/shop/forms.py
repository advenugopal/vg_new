from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form_control', 'placeholder':'Name of the product'}),
            'price':forms.NumberInput(attrs={'class':'form_control', 'placeholder':'Enter the price'}),
            'desc':forms.Textarea(attrs={'class':'form_control', 'placeholder':'description'}),
            'image':forms.ClearableFileInput(attrs={'class':'form_control'}),
            'category':forms.Select(attrs={'class':'form_control'}),
            'stock':forms.NumberInput(attrs={'class':'form_control', 'placeholder':'number of stocks avaialble'}),
        }