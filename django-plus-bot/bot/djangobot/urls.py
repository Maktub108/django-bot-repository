from django.contrib import admin  # Добавьте этот импорт
from django.urls import path
from bot.views import RegisterUserView, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Главная страница
    path('admin/', admin.site.urls),  # Теперь admin будет доступен
    path('api/register/', RegisterUserView.as_view(), name='register_user'),
]