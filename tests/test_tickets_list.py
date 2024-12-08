import pytest
from rest_framework import status


@pytest.mark.django_db
def test_list_tickets(auth_manager, manager_user):
    auth_manager.login(user=manager_user)
    response = auth_manager.get('/api/tickets/')

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_permission_denied(auth_client, client_user):
    auth_client.login(user=client_user)
    response = auth_client.get('/api/tickets/')

    assert response.status_code == status.HTTP_403_FORBIDDEN
