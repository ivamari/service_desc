from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tickets.views.messages import MessageViewSet
from tickets.views.tickets import TicketView

router = DefaultRouter()
router.register(r'tickets', TicketView, basename='ticket')

urlpatterns = [
    path('tickets/<int:id>/messages/',
         MessageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('', include(router.urls)),
]
