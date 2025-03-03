from django.contrib import admin
from .models import HeroBanner, CourseCategory, Course, Review, Event, Inquiry

@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    list_editable = ('is_active', 'order')

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_featured', 'is_active', 'created_at')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_featured', 'is_active')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'rating', 'is_featured', 'is_approved', 'created_at')
    list_filter = ('course', 'rating', 'is_featured', 'is_approved')
    search_fields = ('name', 'content')
    list_editable = ('is_featured', 'is_approved')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active', 'created_at')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
