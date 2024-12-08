from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet

from tickets.models.tickets import Ticket
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
