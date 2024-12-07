from django.contrib import admin

from tickets.models.tickets import Ticket, TicketStatus


@admin.register(TicketStatus)
class TicketStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', )
    list_display_links = ('code', )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'created_at', 'manager')
    list_display_links = ('client',)
