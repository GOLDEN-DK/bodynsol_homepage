from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# 기본 모델 (타임스탬프 필드를 포함하는 추상 모델)
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# 히어로 배너 모델
class HeroBanner(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='제목')
    subtitle = models.CharField(max_length=300, blank=True, verbose_name='부제목')
    image = models.ImageField(upload_to='banners/', verbose_name='배너 이미지')
    button_text = models.CharField(max_length=50, blank=True, verbose_name='버튼 텍스트')
    button_url = models.CharField(max_length=200, blank=True, verbose_name='버튼 URL')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    order = models.PositiveIntegerField(default=0, verbose_name='표시 순서')

    class Meta:
        verbose_name = '히어로 배너'
        verbose_name_plural = '히어로 배너'
        ordering = ['order']

    def __str__(self):
        return self.title

# 교육 과정 카테고리 모델
class CourseCategory(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name='카테고리명')
    slug = models.SlugField(unique=True, verbose_name='슬러그')
    description = models.TextField(blank=True, verbose_name='설명')
    image = models.ImageField(upload_to='categories/', blank=True, verbose_name='카테고리 이미지')
    order = models.PositiveIntegerField(default=0, verbose_name='표시 순서')

    class Meta:
        verbose_name = '교육 과정 카테고리'
        verbose_name_plural = '교육 과정 카테고리'
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# 교육 과정 모델
class Course(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='과정명')
    slug = models.SlugField(unique=True, verbose_name='슬러그')
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses', verbose_name='카테고리')
    description = models.TextField(verbose_name='과정 설명')
    thumbnail = models.ImageField(upload_to='courses/', verbose_name='썸네일')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='수강료')
    duration = models.CharField(max_length=100, verbose_name='교육 기간')
    schedule = models.TextField(blank=True, verbose_name='일정')
    curriculum = models.TextField(blank=True, verbose_name='커리큘럼')
    is_featured = models.BooleanField(default=False, verbose_name='추천 과정 여부')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')

    class Meta:
        verbose_name = '교육 과정'
        verbose_name_plural = '교육 과정'
        ordering = ['-is_featured', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# 수강생 후기 모델
class Review(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews', verbose_name='교육 과정')
    name = models.CharField(max_length=100, verbose_name='이름')
    content = models.TextField(verbose_name='후기 내용')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='평점')
    image = models.ImageField(upload_to='reviews/', blank=True, verbose_name='후기 이미지')
    is_featured = models.BooleanField(default=False, verbose_name='추천 후기 여부')
    is_approved = models.BooleanField(default=False, verbose_name='승인 여부')

    class Meta:
        verbose_name = '수강생 후기'
        verbose_name_plural = '수강생 후기'
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"{self.name}의 {self.course} 후기"

# 이벤트/프로모션 모델
class Event(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='이벤트명')
    slug = models.SlugField(unique=True, verbose_name='슬러그')
    description = models.TextField(verbose_name='이벤트 설명')
    image = models.ImageField(upload_to='events/', verbose_name='이벤트 이미지')
    start_date = models.DateField(verbose_name='시작일')
    end_date = models.DateField(verbose_name='종료일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')

    class Meta:
        verbose_name = '이벤트/프로모션'
        verbose_name_plural = '이벤트/프로모션'
        ordering = ['-start_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# 상담/문의 모델
class Inquiry(TimeStampedModel):
    STATUS_CHOICES = (
        ('pending', '대기중'),
        ('in_progress', '처리중'),
        ('completed', '완료'),
    )
    
    name = models.CharField(max_length=100, verbose_name='이름')
    email = models.EmailField(verbose_name='이메일')
    phone = models.CharField(max_length=20, verbose_name='연락처')
    subject = models.CharField(max_length=200, verbose_name='제목')
    message = models.TextField(verbose_name='문의 내용')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='처리 상태')
    response = models.TextField(blank=True, verbose_name='답변')

    class Meta:
        verbose_name = '상담/문의'
        verbose_name_plural = '상담/문의'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name}의 문의: {self.subject}"
