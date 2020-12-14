from django.forms import ModelForm
from .models import Expenses

from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(ModelForm):
    class Meta:

        model = Expenses
        widgets = {'date': DateInput()}
        # datefield = forms.DateField(widget=DateInput)
        fields = ['date', 'description', 'cost']
