from django import forms

class ProductForm(forms.Form):
    PRODUCT_CATEGORIES = [
        ('food', 'Food'),
        ('snacks', 'Snacks'),
        ('drinks', 'Drinks'),
        ('hardware', 'Hardware'),
    ]
    name = forms.CharField(label='Product Name', max_length=100)
    category = forms.ChoiceField(label='Category', choices=PRODUCT_CATEGORIES)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    rating = forms.IntegerField(label='Rating')
