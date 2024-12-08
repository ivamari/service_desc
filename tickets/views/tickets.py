from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema_view, extend_schema

from tickets.models.messages import Message
from tickets.models.tickets import Ticket, TicketStatus
from tickets.permissions import IsManager
from tickets.serializers.tickets import TicketSerializer
from tickets.services import EmailService


@extend_schema_view(
    list=extend_schema(summary='Список обращений',
                       tags=['Обращения | Менеджеры']),
)
class TicketView(GenericViewSet, mixins.ListModelMixin):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsManager]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('status',)
    ordering = ('created_at',)

    @extend_schema(
        summary='Назначить обращение текущему менеджеру',
        tags=['Обращения | Менеджеры'],
        request=None,
    )
    @action(methods=['POST'], detail=True, url_path='assign-to-me')
    def assign_to_me(self, request, pk=None):
        ticket = self.get_object()

        if ticket.manager is not None:
            return Response({'error': 'Ticket already assigned'}, status=400)

        if request.user.role != 'manager':
            return Response({'error': 'Permission denied'}, status=403)

        ticket.manager = request.user
        ticket.status = TicketStatus.objects.get(code='in_progress')
        ticket.save()

        return Response({'message': 'Ticket assigned successfully'})

    @extend_schema(
        summary='Закрыть обращение',
        tags=['Обращения | Менеджеры'],
        request=None,
    )
    @action(methods=['POST'], detail=True, url_path='close')
    def close_ticket(self, request, pk=None):
        ticket = self.get_object()
        if ticket.status == TicketStatus.objects.get(code='closed'):
            return Response({'error': 'Ticket already closed'}, status=400)
        ticket.status = TicketStatus.objects.get(code='closed')
        ticket.save()

        message = Message.objects.create(
            ticket=ticket,
            user=request.user,
            text='Ваше обращение закрыто. Спасибо за обращение!'
        )

        EmailService.send_email(
            from_email='noreply@service_desc.com',
            to_email=ticket.client.email,
            subject="Ваше обращение закрыто",
            text=message.text
        )
        return Response({'message': 'Ticket closed successfully'})
