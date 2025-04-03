from rest_framework import serializers
from .models import Category, Expense, GroupExpense, ExpenseShare

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'category', 'amount', 'description', 'date']

class ExpenseShareSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = ExpenseShare
        fields = ['id', 'user', 'username', 'share_amount', 'paid']

class GroupExpenseSerializer(serializers.ModelSerializer):
    shares = ExpenseShareSerializer(source='expenseshare_set', many=True, read_only=True)
    
    class Meta:
        model = GroupExpense
        fields = ['id', 'name', 'amount', 'description', 'date', 'shares'] 