# Generated by Django 5.1.5 on 2025-02-23 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("practise3", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("carbs", models.FloatField()),
                ("proteins", models.FloatField()),
                ("fats", models.FloatField()),
                ("calories", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Consume",
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
                ("date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "food_consumed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="practise3.food"
                    ),
                ),
            ],
        ),
    ]
