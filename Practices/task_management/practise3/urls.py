from django.urls import path
from . import views

urlpatterns = [
    path('chart-data/', views.nutrient_data, name="chart-data"),
]

urlpatterns += [
    path('set-goals/', views.set_goals, name="set-goals"),
]

urlpatterns += [
    path('', views.index, name='index'),
    path('chart-data/', views.chart_data, name='chart-data'),
]

urlpatterns += [
    path('register/', views.register, name="register"),
]