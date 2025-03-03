from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    """
    API의 루트 엔드포인트
    """
    return Response({
        'status': 'API is running',
        'version': '1.0.0',
        'endpoints': {
            # 여기에 API 엔드포인트 추가 예정
            # 'courses': reverse('course-list', request=request, format=format),
            # 'reviews': reverse('review-list', request=request, format=format),
        }
    })
