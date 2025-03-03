from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# 여기에 ViewSet 등록 예정
# router.register('courses', views.CourseViewSet)
# router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),
    # 여기에 추가 URL 패턴 등록
]

urlpatterns += router.urls 