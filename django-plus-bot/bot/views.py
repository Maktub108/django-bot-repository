from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TelegramUser
from .serializers import TelegramUserSerializer, RegisterUserSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home_view(request):
    return HttpResponse("""
        <h1>Добро пожаловать в Django + Telegram Bot API!</h1>
        <p>Доступные эндпоинты:</p>
        <ul>
            <li><a href="/api/register/">/api/register/</a> – Регистрация пользователя (POST)</li>
            <li><a href="/admin/">/admin/</a> – Админ-панель</li>
        </ul>
    """)

class RegisterUserView(APIView):
    def post(self, request):
        # Валидация входных данных
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_id = serializer.validated_data['user_id']
        username = serializer.validated_data['username']

        # Попытка создать или получить существующего пользователя
        user, created = TelegramUser.objects.get_or_create(
            user_id=user_id,
            defaults={'username': username}
        )

        if created:
            return Response({"status": "success", "message": "Зарегистрирован!"}, status=201)
        return Response({"status": "updated", "message": "Данные обновлены!"}, status=200)




