from app.routes.route_utilities import validate_model
from werkzeug.exceptions import HTTPException
from app.models.planet import Planet
import pytest

def test_validate_planet(two_saved_planets):
    result_planet = validate_model(Planet, 1)

    assert result_planet.id == 1
    assert result_planet.name == "Mercury"
    assert result_planet.description == "the smallest planet"
    assert result_planet.color == "gray"

def test_validate_model_missing_record(two_saved_planets):
    with pytest.raises(HTTPException) as error:
        result_planet = validate_model(Planet, "3")

    response = error.value.response
    assert response.status == "404 NOT FOUND"

def test_validate_model_planet_invalid_id(two_saved_planets):
    with pytest.raises(HTTPException) as error:
        result_planet = validate_model(Planet, "cat")

    response = error.value.response
    assert response.status == "400 BAD REQUEST"


