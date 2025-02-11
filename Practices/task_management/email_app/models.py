from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='cv_pictures/', blank=True, null=True)
    resume_file = models.FileField(upload_to='cv_resumes/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
