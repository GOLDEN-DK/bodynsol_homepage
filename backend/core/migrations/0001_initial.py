# Generated by Django 5.0.2 on 2025-03-03 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CourseCategory",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="카테고리명")),
                ("slug", models.SlugField(unique=True, verbose_name="슬러그")),
                ("description", models.TextField(blank=True, verbose_name="설명")),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="categories/", verbose_name="카테고리 이미지"
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0, verbose_name="표시 순서")),
            ],
            options={
                "verbose_name": "교육 과정 카테고리",
                "verbose_name_plural": "교육 과정 카테고리",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200, verbose_name="이벤트명")),
                ("slug", models.SlugField(unique=True, verbose_name="슬러그")),
                ("description", models.TextField(verbose_name="이벤트 설명")),
                (
                    "image",
                    models.ImageField(upload_to="events/", verbose_name="이벤트 이미지"),
                ),
                ("start_date", models.DateField(verbose_name="시작일")),
                ("end_date", models.DateField(verbose_name="종료일")),
                ("is_active", models.BooleanField(default=True, verbose_name="활성화 여부")),
            ],
            options={
                "verbose_name": "이벤트/프로모션",
                "verbose_name_plural": "이벤트/프로모션",
                "ordering": ["-start_date"],
            },
        ),
        migrations.CreateModel(
            name="HeroBanner",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200, verbose_name="제목")),
                (
                    "subtitle",
                    models.CharField(blank=True, max_length=300, verbose_name="부제목"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="banners/", verbose_name="배너 이미지"),
                ),
                (
                    "button_text",
                    models.CharField(blank=True, max_length=50, verbose_name="버튼 텍스트"),
                ),
                (
                    "button_url",
                    models.CharField(blank=True, max_length=200, verbose_name="버튼 URL"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="활성화 여부")),
                ("order", models.PositiveIntegerField(default=0, verbose_name="표시 순서")),
            ],
            options={
                "verbose_name": "히어로 배너",
                "verbose_name_plural": "히어로 배너",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Inquiry",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="이름")),
                ("email", models.EmailField(max_length=254, verbose_name="이메일")),
                ("phone", models.CharField(max_length=20, verbose_name="연락처")),
                ("subject", models.CharField(max_length=200, verbose_name="제목")),
                ("message", models.TextField(verbose_name="문의 내용")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "대기중"),
                            ("in_progress", "처리중"),
                            ("completed", "완료"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="처리 상태",
                    ),
                ),
                ("response", models.TextField(blank=True, verbose_name="답변")),
            ],
            options={
                "verbose_name": "상담/문의",
                "verbose_name_plural": "상담/문의",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Course",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200, verbose_name="과정명")),
                ("slug", models.SlugField(unique=True, verbose_name="슬러그")),
                ("description", models.TextField(verbose_name="과정 설명")),
                (
                    "thumbnail",
                    models.ImageField(upload_to="courses/", verbose_name="썸네일"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=0, max_digits=10, verbose_name="수강료"
                    ),
                ),
                ("duration", models.CharField(max_length=100, verbose_name="교육 기간")),
                ("schedule", models.TextField(blank=True, verbose_name="일정")),
                ("curriculum", models.TextField(blank=True, verbose_name="커리큘럼")),
                (
                    "is_featured",
                    models.BooleanField(default=False, verbose_name="추천 과정 여부"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="활성화 여부")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="courses",
                        to="core.coursecategory",
                        verbose_name="카테고리",
                    ),
                ),
            ],
            options={
                "verbose_name": "교육 과정",
                "verbose_name_plural": "교육 과정",
                "ordering": ["-is_featured", "title"],
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="이름")),
                ("content", models.TextField(verbose_name="후기 내용")),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        verbose_name="평점",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="reviews/", verbose_name="후기 이미지"
                    ),
                ),
                (
                    "is_featured",
                    models.BooleanField(default=False, verbose_name="추천 후기 여부"),
                ),
                (
                    "is_approved",
                    models.BooleanField(default=False, verbose_name="승인 여부"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="core.course",
                        verbose_name="교육 과정",
                    ),
                ),
            ],
            options={
                "verbose_name": "수강생 후기",
                "verbose_name_plural": "수강생 후기",
                "ordering": ["-is_featured", "-created_at"],
            },
        ),
    ]
