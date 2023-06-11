import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"
unique_id = 9144154627


def test_get_posts():
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100


@pytest.mark.parametrize("user_id, title, body", [
    (unique_id, "Test title 1", "Test body 1"),
    (unique_id, "Test title 2", "Test body 2"),
    (unique_id, "Test title 3", "Test body 3")
])
def test_post_posts(user_id, title, body):
    data = {"userId": user_id, "title": title, "body": body}
    response = requests.post(f"{base_url}/posts", json=data)
    assert response.status_code == 201
    assert response.json()["userId"] == user_id
    assert response.json()["title"] == title
    assert response.json()["body"] == body


@pytest.mark.parametrize("post_id", [
    1,
    100
])
def test_delete_posts(post_id):
    response = requests.delete(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
