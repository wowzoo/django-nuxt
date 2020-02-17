import pytest
from core.models import Recipe
from core.serializers import RecipeSerializer


@pytest.mark.django_db
def test_recipe():
    recipe = Recipe(
        name='Cream Pie',
        ingredients='cream',
        difficulty='easy',
        prep_time=23,
        prep_guide='cream'
    )

    serializer = RecipeSerializer(recipe)

    assert serializer.data == {
        'id': None,
        'name': 'Cream Pie',
        'ingredients': 'cream',
        'difficulty': 'easy',
        'picture': None,
        'prep_time': 23,
        'prep_guide': 'cream'
    }
