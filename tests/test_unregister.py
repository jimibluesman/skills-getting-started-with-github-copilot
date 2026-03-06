def test_unregister_success(client):
    # First signup
    client.post("/activities/Chess Club/signup", params={"email": "test@example.com"})
    # Then unregister
    response = client.delete("/activities/Chess Club/unregister", params={"email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Unregistered test@example.com from Chess Club" == data["message"]


def test_unregister_activity_not_found(client):
    response = client.delete("/activities/NonExistent/unregister", params={"email": "test@example.com"})
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" == data["detail"]


def test_unregister_not_signed_up(client):
    response = client.delete("/activities/Chess Club/unregister", params={"email": "notsigned@example.com"})
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student is not signed up for this activity" == data["detail"]