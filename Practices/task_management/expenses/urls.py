from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'expenses', views.ExpenseViewSet, basename='expense')
router.register(r'group-expenses', views.GroupExpenseViewSet, basename='group-expense')

urlpatterns = [
    path('', include(router.urls)),
] 