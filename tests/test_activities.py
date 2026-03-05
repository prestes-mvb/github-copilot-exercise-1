def test_get_activities_returns_activity_dictionary(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities

    for details in activities.values():
        assert expected_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
