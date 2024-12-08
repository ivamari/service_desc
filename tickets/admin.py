from django.contrib import admin

from tickets.models.messages import Message
from tickets.models.tickets import Ticket, TicketStatus


@admin.register(TicketStatus)
class TicketStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    list_display_links = ('code',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'created_at', 'manager',)
    list_display_links = ('id', 'client',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'created_at', 'text',)
    list_display_links = ('ticket',)
