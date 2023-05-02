from django import forms

from .models import Author, Book, Publisher, Store


class BookModelForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
    pubdate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    stores = forms.ModelMultipleChoiceField(
        queryset=Store.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Book
        fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate', 'stores']
