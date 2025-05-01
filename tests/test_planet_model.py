from app.models.planet import Planet
import pytest

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Neptune",
        "description": "Windy Planet",
        "color": "gray"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Neptune"
    assert new_planet.description == "Windy Planet"
    assert new_planet.color == "gray"

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "Windy Planet",
        "color": "gray"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Neptune",
        "color": "gray"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "size": "some stuff",
        "name": "Neptune",
        "description": "Windy planet",
        "color": "gray"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Neptune"
    assert new_planet.description == "Windy planet"
    assert new_planet.color == "gray"

def test_to_dict_no_missing_data():
    test_data = Planet(id = 1,
                    name = "Mercury",
                    description = "smallest planet",
                    color = "gray")
    
    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "smallest planet"
    assert result["color"] == "gray"

def test_to_dict_missing_id():
    test_data = Planet(name="Mercury",
                    description="smallest planet")
    
    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["color"] is None
    assert result["description"] == "smallest planet"

def test_to_dict_missing_name():
    test_data = Planet(id=1, 
                    description= "smallest planet",
                    color="gray")
    
    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "smallest planet"
    assert result["color"] == "gray"

def test_to_dict_missing_description():
    test_data = Planet(id=1, name="Mercury")
    
    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["color"] is None