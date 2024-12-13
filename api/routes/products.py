from flask import Blueprint, jsonify, request
from models.products import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    name = request.args.get('name')
    category = request.args.get('category')
    
    query = Product.query
    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))
    if category:
        query = query.filter_by(category=category)
    
    products = query.all()
    return jsonify([product.to_dict() for product in products]), 200