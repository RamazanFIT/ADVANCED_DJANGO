from django.urls import path

from .views import contact_view, success_page

urlpatterns = [

    path('contact/', contact_view, name='contact'),
    path('success/', success_page, name='success_page'),

]