from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    registered_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.username} ({self.user_id})"

