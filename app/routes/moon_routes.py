from flask import Blueprint, request, make_response, abort
from app.models.moon import Moon
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()

    return create_model(Moon, request_body)

    # try:
    #     new_moon = Moon.from_dict(request_body)
        
    # except KeyError as error:
    #     response = {"message": f"Invalid request: missing {error.args[0]}"}
    #     abort(make_response(response, 400))
    
    # db.session.add(new_moon)
    # db.session.commit()

    # return make_response(new_moon.to_dict(), 201)

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)
    # query = db.select(Moon)

    # name_param = request.args.get("name")
    # if name_param:
    #     query = query.where(Moon.name.ilike(f"%{name_param}%"))

    # moons = db.session.scalars(query.order_by(Moon.id))
    # # Use list comprehension syntax to create the list `authors_response`
    # moons_response = [moon.to_dict() for moon in moons]

    # return moons_response
