from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tickets.models.tickets import Ticket, TicketStatus
from tickets.permissions import IsManager
from tickets.serializers.tickets import TicketSerializer


@extend_schema_view(
    list=extend_schema(summary='Список обращений', tags=['Обращения']),
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
        tags=['Обращения'],
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
        ticket.status = TicketStatus.objects.filter(code='in_progress').first()
        ticket.save()

        return Response({'message': 'Ticket assigned successfully'})
