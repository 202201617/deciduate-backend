# Generated by Django 5.0.4 on 2024-05-28 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("major", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompulsorySubject",
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
                ("status", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("main_major", models.IntegerField(default=0)),
                ("double_major", models.IntegerField(default=0)),
                ("second_major", models.IntegerField(default=0)),
                ("outside", models.IntegerField(default=0)),
                ("liberal", models.IntegerField(default=0)),
                ("minor_major", models.IntegerField(default=0)),
                ("teaching", models.IntegerField(default=0)),
                ("self_selection", models.IntegerField(default=0)),
                ("total_credit", models.IntegerField(default=0)),
                ("total_score", models.FloatField(default=0)),
                ("main_test_pass", models.BooleanField(default=False)),
                ("double_test_pass", models.BooleanField(default=False)),
                (
                    "foreign_pass",
                    models.IntegerField(
                        choices=[
                            (1, "해당없음"),
                            (2, "FLEX"),
                            (3, "FLEX 스피킹"),
                            (4, "TOEIC"),
                            (5, "TOEIC 스피킹"),
                            (6, "TOEFL"),
                            (7, "IELTS"),
                            (8, "OPIc"),
                            (9, "외국어인증대체과정"),
                        ],
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Basic",
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
                (
                    "nickname",
                    models.CharField(max_length=20, unique=True, verbose_name="닉네임"),
                ),
                (
                    "student_no",
                    models.CharField(
                        max_length=10, null=True, unique=True, verbose_name="학번"
                    ),
                ),
                (
                    "major_type",
                    models.IntegerField(
                        choices=[(1, "전공심화"), (2, "이중전공"), (3, "부전공"), (4, "전공심화+부전공")],
                        default=1,
                        verbose_name="전공유형",
                    ),
                ),
                (
                    "transfer",
                    models.BooleanField(blank=True, default=False, verbose_name="편입생"),
                ),
                (
                    "foreign",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="외국인전형"
                    ),
                ),
                (
                    "double_major",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="users_double",
                        to="major.major",
                        verbose_name="이중전공",
                    ),
                ),
                (
                    "main_major",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="users_main",
                        to="major.major",
                        verbose_name="본전공",
                    ),
                ),
                (
                    "minor_major",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="users_minor",
                        to="major.major",
                        verbose_name="부전공",
                    ),
                ),
            ],
        ),
    ]
