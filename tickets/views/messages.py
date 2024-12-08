from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema_view, extend_schema

from tickets.models.messages import Message
from tickets.models.tickets import Ticket, TicketStatus
from tickets.permissions import IsManager
from tickets.serializers.messages import (
    MessageListSerializer,
    MessageCreateSerializer
)
from tickets.serializers.mixins import ExtendedView
from tickets.services import EmailService


@extend_schema_view(
    list=extend_schema(summary='Список сообщений',
                       tags=['Сообщения | Менеджеры']),
    create=extend_schema(summary='Создать сообщение',
                         tags=['Сообщения | Менеджеры']),
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
            from_email='noreply@service_desc.com',
            to_email=ticket.client.email,
            subject="Ответ на ваше обращение",
            text=message.text
        )


@extend_schema_view(
    create=extend_schema(summary='Создать обращение',
                         tags=['Обращения | Клиенты']),
)
class ClientMessagesViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = MessageCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user

        ticket = Ticket.objects.filter(
            client=user, status__in=('new', 'in_progress')).first()

        if not ticket:
            ticket = Ticket.objects.create(
                client=user,
                status=TicketStatus.objects.get(code='new'),
            )

        serializer.save(ticket=ticket, user=user)

        message = Message.objects.create(
            ticket=ticket,
            user=None,
            text="Ваше сообщение получено. Мы скоро свяжемся с вами."
        )

        EmailService.send_email(
            from_email='noreply@service_desc.com',
            to_email=user.email,
            subject="Ваше сообщение получено",
            text=message.text
        )
