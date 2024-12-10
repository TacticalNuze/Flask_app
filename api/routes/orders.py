from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return {"message": "Welcome to the Shop App API!"}, 200
