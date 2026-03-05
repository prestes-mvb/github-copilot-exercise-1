from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    original_activities = deepcopy(activities)

    # Arrange: reset shared in-memory state before each test.
    activities.clear()
    activities.update(deepcopy(original_activities))

    yield

    activities.clear()
    activities.update(deepcopy(original_activities))
