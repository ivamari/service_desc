from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema_view, extend_schema

from tickets.models.messages import Message
from tickets.models.tickets import Ticket
from tickets.permissions import IsManager
from tickets.serializers.messages import (
    MessageListSerializer,
    MessageCreateSerializer
)
from tickets.serializers.mixins import ExtendedView
from tickets.services import EmailService


@extend_schema_view(
    list=extend_schema(summary='Список сообщений', tags=['Сообщения']),
    create=extend_schema(summary='Создать сообщение',
                         tags=['Сообщения']),
)
class MessageViewSet(ExtendedView, GenericViewSet, mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    permission_classes = [IsManager]
    http_method_names = ('get', 'post',)

    lookup_url_kwarg = 'id'

    multi_serializer_class = {
        'list': MessageListSerializer,
        'create': MessageCreateSerializer,
    }

    def get_queryset(self):
        ticket_id = self.kwargs.get('id')
        return Message.objects.filter(ticket_id=ticket_id)

    def perform_create(self, serializer):
        ticket_id = self.kwargs.get('id')
        ticket = Ticket.objects.get(id=ticket_id)

        message = serializer.save(user=self.request.user, ticket=ticket)

        EmailService.send_email(
            from_email=self.request.user.email,
            to_email=ticket.client.email,
            subject="Ответ на ваше обращение",
            text=message.message
        )
