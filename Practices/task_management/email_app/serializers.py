from rest_framework import serializers
from .models import CV


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'  # Сериализуем все поля модели
        read_only_fields = ('ai_score', 'processing_status', 'ai_feedback', 
                          'skills', 'experience', 'education')

class CVDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'
