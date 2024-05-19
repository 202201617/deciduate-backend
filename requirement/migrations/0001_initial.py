# Generated by Django 4.2 on 2024-05-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Requirement",
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
                ("student_no", models.IntegerField(default=0)),
                ("main_major", models.IntegerField(default=0)),
                ("double_major", models.IntegerField(default=0)),
                ("minor_major", models.IntegerField(default=0)),
                ("liberal", models.IntegerField(default=0)),
                ("self_selection", models.IntegerField(default=0)),
                ("total_credit", models.IntegerField(default=0)),
                ("test_type", models.CharField(max_length=10)),
                ("flex", models.IntegerField(default=0)),
                ("flex_speaking", models.IntegerField(default=0)),
                ("toeic", models.IntegerField(default=0)),
                ("toeic_speaking", models.IntegerField(default=0)),
                ("opic", models.CharField(max_length=5)),
            ],
        ),
    ]
