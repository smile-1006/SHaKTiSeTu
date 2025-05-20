from flask import Blueprint, jsonify, request
from src.models.marketplace import Product, Order, ProductRecommendation
from src.models.user import db

marketplace_bp = Blueprint('marketplace', __name__)

# Product endpoints
@marketplace_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@marketplace_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

@marketplace_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'description', 'price', 'category', 'seller_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        seller_id=data['seller_id'],
        image_url=data.get('image_url')
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify(product.to_dict()), 201

@marketplace_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(product, key):
            setattr(product, key, value)
    
    db.session.commit()
    return jsonify(product.to_dict())

@marketplace_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

# Order endpoints
@marketplace_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@marketplace_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict())

@marketplace_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('buyer_id', 'seller_id', 'product_id', 'total_price')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    order = Order(
        buyer_id=data['buyer_id'],
        seller_id=data['seller_id'],
        product_id=data['product_id'],
        quantity=data.get('quantity', 1),
        total_price=data['total_price'],
        status=data.get('status', 'pending')
    )
    
    db.session.add(order)
    db.session.commit()
    
    return jsonify(order.to_dict()), 201

@marketplace_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(order, key):
            setattr(order, key, value)
    
    db.session.commit()
    return jsonify(order.to_dict())

# AI Recommendation endpoints
@marketplace_bp.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    recommendations = ProductRecommendation.query.filter_by(user_id=user_id).order_by(ProductRecommendation.score.desc()).all()
    return jsonify([rec.to_dict() for rec in recommendations])

@marketplace_bp.route('/recommendations/generate', methods=['POST'])
def generate_recommendations():
    # This would typically call an AI service to generate recommendations
    # For now, we'll just return a placeholder response
    return jsonify({'message': 'Recommendation generation initiated'}), 202
