from rest_framework import serializers

from tickets.models.tickets import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = (
            'id',
            'client',
            'status',
            'created_at',
            'manager',
        )
