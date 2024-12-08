from rest_framework import serializers

from tickets.models.messages import Message


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'ticket',
            'user',
            'created_at',
            'text',
        )


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'text',
        )
