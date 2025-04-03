from django.contrib import admin
from .models import Category, Expense, GroupExpense, ExpenseShare

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'category', 'date', 'user')
    list_filter = ('category', 'date', 'user')
    search_fields = ('description',)
    date_hierarchy = 'date'

@admin.register(GroupExpense)
class GroupExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'created_by')
    list_filter = ('date', 'created_by')
    search_fields = ('name', 'description')

@admin.register(ExpenseShare)
class ExpenseShareAdmin(admin.ModelAdmin):
    list_display = ('user', 'group_expense', 'share_amount', 'paid')
    list_filter = ('paid', 'user')
    search_fields = ('user__username', 'group_expense__name')
