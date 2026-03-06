def test_signup_success(client):
    response = client.post("/activities/Chess Club/signup", params={"email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Signed up test@example.com for Chess Club" == data["message"]


def test_signup_activity_not_found(client):
    response = client.post("/activities/NonExistent/signup", params={"email": "test@example.com"})
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" == data["detail"]


def test_signup_already_signed_up(client):
    # First signup
    client.post("/activities/Chess Club/signup", params={"email": "test@example.com"})
    # Second attempt
    response = client.post("/activities/Chess Club/signup", params={"email": "test@example.com"})
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student is already signed up for this activity" == data["detail"]