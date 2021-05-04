import pytest
from ..models import Cheese
pytestmark = pytest.mark.django_db
from .factories import CheeseFactory
def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
