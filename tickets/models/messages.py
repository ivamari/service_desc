from django.contrib.auth import get_user_model
from django.db import models

from tickets.models.tickets import Ticket

User = get_user_model()


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, models.SET_NULL,
                               'messages', null=True,
                               verbose_name='Обращение')
    user = models.ForeignKey(User, models.SET_NULL,
                             'messages', null=True,
                             verbose_name='Пользователь')
    created_at = models.DateTimeField('Дата создания',
                                      auto_now_add=True)
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение {self.pk}'
