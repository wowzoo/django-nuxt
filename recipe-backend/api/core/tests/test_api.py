import pytest

from django.shortcuts import reverse


@pytest.mark.django_db
def test_recipe_post(api_client):
    data = {
        "name": "Meat Pie",
        "ingredients": "meat",
        "difficulty": "Medium",
        "prep_time": 60,
        "prep_guide": "cook meat pie"
    }

    response = api_client.post('/api/recipes/', data=data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_recipe_get(api_client):
    response = api_client.get('/api/recipes/')

    assert response.status_code == 200
    assert response.data == []
