from flask import Blueprint, abort, make_response
# from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")










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

# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return dict(
#         id = planet.id,
#         name = planet.name,
#         description = planet.description,
#         color = planet.color
#     )

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))
        