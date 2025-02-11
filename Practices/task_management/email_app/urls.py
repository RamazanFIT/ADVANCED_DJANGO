from django.urls import path

from .views import share_cv_email, CVListCreateView, CVRetrieveUpdateDestroyView, cv_list

urlpatterns = [

    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'),
    path('api/cvs/', CVListCreateView.as_view(), name='cv-list-create'),  # Получение списка и создание
    path('api/cvs/<int:pk>/', CVRetrieveUpdateDestroyView.as_view(), name='cv-detail'),
    # Получение, обновление и удаление
    path('cvs/', cv_list, name='cv_list'),  # Создаем путь для отображения cv_list

]
