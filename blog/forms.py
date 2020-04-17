from django import forms
from .models import Category

class PostForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '7' }),
        required=True
    )

    category = forms.CharField(
        label='Category',
        widget=forms.Select(attrs={'class': 'form-control'}, choices=[(category, category) for category in Category.objects.all()]),
        required=True
    )

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )



