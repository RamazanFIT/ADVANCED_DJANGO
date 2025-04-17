from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CV
from .services.ai_analysis import ResumeAnalyzer

User = get_user_model()

class CVTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_cv(self):
        file_content = b'Test resume content'
        resume_file = SimpleUploadedFile(
            "resume.pdf",
            file_content,
            content_type="application/pdf"
        )

        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'resume_file': resume_file
        }

        response = self.client.post('/api/cvs/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CV.objects.count(), 1)

class ResumeAnalyzerTests(TestCase):
    def setUp(self):
        self.analyzer = ResumeAnalyzer()

    def test_extract_skills(self):
        text = "I am proficient in Python and JavaScript"
        doc = self.analyzer.nlp(text)
        skills = self.analyzer._extract_skills(doc)
        self.assertIn('python', [skill.lower() for skill in skills])
        self.assertIn('javascript', [skill.lower() for skill in skills])
