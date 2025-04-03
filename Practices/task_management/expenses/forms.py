from django import forms
from .models import Expense, Category, GroupExpense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class GroupExpenseForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = GroupExpense
        fields = ['name', 'amount', 'description', 'users', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        } 