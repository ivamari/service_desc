import pytest


@pytest.mark.django_db
def test_assign_to_me(auth_manager, manager_user, ticket, ticket_status):
    response = auth_manager.post(f'/api/tickets/{ticket.id}/assign-to-me/')
    assert response.status_code == 200
    assert response.data['message'] == 'Ticket assigned successfully'

    ticket.refresh_from_db()
    assert ticket.manager == manager_user
    assert ticket.status == ticket_status['in_progress']
