from . import models, serializers
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.views.generic.base import TemplateView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
        

class Register(CreateAPIView):
    """
    Добавляет нового пользователя в бд
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]


class Index(TemplateView):
    template_name = 'index.html'