from celery import shared_task
from .models import JobApplication
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@shared_task
def calculate_match_score(application_id):
    try:
        application = JobApplication.objects.get(id=application_id)
        
        # Загружаем модель spaCy
        nlp = spacy.load('en_core_web_lg')
        
        # Получаем текст резюме и описание вакансии
        cv_text = application.cv.get_text_content()  # Метод для получения текста из резюме
        job_description = application.job.description
        
        # Создаем TF-IDF векторайзер
        vectorizer = TfidfVectorizer(stop_words='english')
        
        # Преобразуем тексты в векторы
        vectors = vectorizer.fit_transform([cv_text, job_description])
        
        # Вычисляем косинусное сходство
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        
        # Обновляем score заявки
        application.match_score = similarity * 100  # Переводим в проценты
        application.save()
        
        return True
        
    except Exception as e:
        print(f"Error calculating match score: {e}")
        return False 