from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Category, Expense, GroupExpense, ExpenseShare
from .serializers import (
    CategorySerializer,
    ExpenseSerializer,
    GroupExpenseSerializer,
)

# Create your views here.

class ExpenseFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')
    
    class Meta:
        model = Expense
        fields = ['category', 'date_from', 'date_to']

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ExpenseFilter

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GroupExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = GroupExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GroupExpense.objects.filter(
            participants=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        group_expense = serializer.save(created_by=self.request.user)
        total_participants = len(self.request.data.get('participants', [])) + 1
        share_amount = group_expense.amount / total_participants
        
        # Create share for creator
        ExpenseShare.objects.create(
            user=self.request.user,
            group_expense=group_expense,
            share_amount=share_amount
        )
        
        # Create shares for other participants
        for user_id in self.request.data.get('participants', []):
            ExpenseShare.objects.create(
                user_id=user_id,
                group_expense=group_expense,
                share_amount=share_amount
            )
