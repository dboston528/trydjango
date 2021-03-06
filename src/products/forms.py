from django import forms

from .models import Product

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields  = [
            'title',
            'description',
            'price'
        ]
        
# different form fields here -> https://docs.djangoproject.com/en/2.1/ref/forms/fields/
# https://docs.djangoproject.com/en/2.1/ref/forms/widgets/
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                            attrs={ 
                                                                'placeholder': "Your description",
                                                                'class': 'new-class-name two',
                                                                'id': 'my-id-for-textarea',
                                                                'rows': 20,
                                                                'cols': 120
                                                            }
                                                    )
                                        )
    price       = forms.DecimalField(initial=199.99)