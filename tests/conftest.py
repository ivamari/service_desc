import pytest
from rest_framework.test import APIClient
from tickets.models.tickets import Ticket, TicketStatus


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_manager(api_client, manager_user):
    api_client.force_authenticate(user=manager_user)
    return api_client


@pytest.fixture
def auth_client(api_client, client_user):
    api_client.force_authenticate(user=client_user)
    return api_client


@pytest.fixture
def ticket_status():
    new_status = TicketStatus.objects.create(code='new', name='Новое')
    in_progress_status = TicketStatus.objects.create(code='in_progress',
                                                     name='В работе')
    return {'new': new_status, 'in_progress': in_progress_status}


@pytest.fixture
def manager_user(django_user_model):
    return django_user_model.objects.create_user(
        username='manager',
        password='password123',
        role='manager',
        email='manager@example.ru',
    )


@pytest.fixture
def client_user(django_user_model):
    return django_user_model.objects.create_user(
        username='client',
        password='password123',
        role='client',
        email='user@example.ru',
    )


@pytest.fixture
def ticket(ticket_status, client_user):
    return Ticket.objects.create(
        client_id=client_user.id,
        status=ticket_status['new'],
    )
