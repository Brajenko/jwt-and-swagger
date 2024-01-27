from django.shortcuts import redirect
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView


router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user-viewset')

urlpatterns = [
    path('', views.Index.as_view()),
    path('api/', include(router.urls)),
    path('api/token/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('reg/', views.Register.as_view(), name='user_registration'),
    path('api_schema/', get_schema_view(public=True), name='api_schema'),
    path('docs/', TemplateView.as_view(template_name='swagger.html'), name='swagger-ui'),
]