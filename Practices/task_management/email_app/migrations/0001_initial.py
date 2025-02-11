# Generated by Django 5.1.5 on 2025-02-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CV",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="cv_pictures/"),
                ),
                (
                    "resume_file",
                    models.FileField(blank=True, null=True, upload_to="cv_resumes/"),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
