from django import forms
from . models import Good
from django.forms import ModelChoiceField


class GoodsForm(forms.Form):

    how_to_search = forms.BooleanField(required=False, label='Искать во всех разделах:', initial=False)
    search = forms.CharField(max_length=255, required=False, label='', widget=forms.TextInput(attrs={'class': 'search', 'size': 50}))


