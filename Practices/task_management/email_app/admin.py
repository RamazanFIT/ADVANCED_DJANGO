from django.contrib import admin
from .models import CV

@admin.register(CV)  # Регистрация модели через декоратор
class CVAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'date_created')  # Укажите, какие поля отображать в списке
    search_fields = ('name', 'email')  # Разрешаем поиск по этим полям
    list_filter = ('date_created',)  # Фильтрация по дате создания

    # Добавьте другие настройки, если нужно, например:
    # fields = ('name', 'email', 'phone_number', 'profile_picture', 'resume_file')  # Порядок полей в форме
    # или другие параметры админки.