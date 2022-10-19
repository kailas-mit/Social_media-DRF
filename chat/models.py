from django.db import models
from user_auth.models import User

class Chat(models.Model):
    m_sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name='m_sender')
    m_receiver=models.ForeignKey(User, on_delete=models.CASCADE, related_name='m_receiver')
    message=models.CharField(max_length=1200)
    timestamp=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.m_sender}--{self.m_receiver}--{self.message}"

    class Meta:
        ordering=['timestamp']
