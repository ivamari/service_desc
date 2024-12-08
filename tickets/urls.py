from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tickets.views.tickets import TicketView

router = DefaultRouter()
router.register(r'tickets', TicketView, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
]
