from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.routes.route_utilities import validate_model
from ..db import db

bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    try:
        new_planet = Planet.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201


@bp.get("")
def get_all_planets():
    query = db.select(Planet)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    color_param = request.args.get("color")
    if color_param:
        query = query.where(Planet.color.ilike(f"%{color_param}%"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)
    #line above could also be written as:
    #planets = db.session.execute(query).scalars()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())

    return planets_response




# @planets_bp.get("")
# def get_all_planets():
#     result_list = []
#     for planet in planets:
#         result_list.append(dict(
#             id = planet.id,
#             name = planet.name,
#             description = planet.description,
#             color = planet.color
#         ))
#     return result_list

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

