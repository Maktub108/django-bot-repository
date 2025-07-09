from rest_framework import serializers
from .models import TelegramUser

# Для сериализации вывода (чтение)
class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['user_id', 'username', 'registered_at']

# Для валидации ввода (регистрация)
class RegisterUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    username = serializers.CharField(required=False, allow_null=True)

    def validate_user_id(self, value):
        """Проверка, что user_id положительный"""
        if value <= 0:
            raise serializers.ValidationError("User ID должен быть положительным числом")
        return value