from flask import Blueprint, jsonify, request
from src.models.storefront import Storefront, StorefrontSection, SocialIntegration
from src.models.user import db

storefront_bp = Blueprint('storefront', __name__)

# Storefront endpoints
@storefront_bp.route('/storefronts', methods=['GET'])
def get_storefronts():
    storefronts = Storefront.query.all()
    return jsonify([storefront.to_dict() for storefront in storefronts])

@storefront_bp.route('/storefronts/<int:storefront_id>', methods=['GET'])
def get_storefront(storefront_id):
    storefront = Storefront.query.get_or_404(storefront_id)
    return jsonify(storefront.to_dict())

@storefront_bp.route('/storefronts', methods=['POST'])
def create_storefront():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('user_id', 'name')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    storefront = Storefront(
        user_id=data['user_id'],
        name=data['name'],
        description=data.get('description'),
        logo_url=data.get('logo_url'),
        banner_url=data.get('banner_url'),
        theme=data.get('theme', 'default'),
        custom_domain=data.get('custom_domain'),
        is_published=data.get('is_published', False)
    )
    
    db.session.add(storefront)
    db.session.commit()
    
    return jsonify(storefront.to_dict()), 201

@storefront_bp.route('/storefronts/<int:storefront_id>', methods=['PUT'])
def update_storefront(storefront_id):
    storefront = Storefront.query.get_or_404(storefront_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(storefront, key):
            setattr(storefront, key, value)
    
    db.session.commit()
    return jsonify(storefront.to_dict())

@storefront_bp.route('/storefronts/<int:storefront_id>', methods=['DELETE'])
def delete_storefront(storefront_id):
    storefront = Storefront.query.get_or_404(storefront_id)
    db.session.delete(storefront)
    db.session.commit()
    return jsonify({'message': 'Storefront deleted successfully'})

# Storefront Section endpoints
@storefront_bp.route('/storefronts/<int:storefront_id>/sections', methods=['GET'])
def get_sections(storefront_id):
    sections = StorefrontSection.query.filter_by(storefront_id=storefront_id).order_by(StorefrontSection.position).all()
    return jsonify([section.to_dict() for section in sections])

@storefront_bp.route('/storefronts/sections/<int:section_id>', methods=['GET'])
def get_section(section_id):
    section = StorefrontSection.query.get_or_404(section_id)
    return jsonify(section.to_dict())

@storefront_bp.route('/storefronts/<int:storefront_id>/sections', methods=['POST'])
def create_section(storefront_id):
    data = request.get_json()
    
    if not data or not all(k in data for k in ('type',)):
        return jsonify({'error': 'Missing required fields'}), 400
    
    section = StorefrontSection(
        storefront_id=storefront_id,
        title=data.get('title'),
        content=data.get('content'),
        type=data['type'],
        position=data.get('position', 0),
        settings=data.get('settings', {})
    )
    
    db.session.add(section)
    db.session.commit()
    
    return jsonify(section.to_dict()), 201

@storefront_bp.route('/storefronts/sections/<int:section_id>', methods=['PUT'])
def update_section(section_id):
    section = StorefrontSection.query.get_or_404(section_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(section, key):
            setattr(section, key, value)
    
    db.session.commit()
    return jsonify(section.to_dict())

@storefront_bp.route('/storefronts/sections/<int:section_id>', methods=['DELETE'])
def delete_section(section_id):
    section = StorefrontSection.query.get_or_404(section_id)
    db.session.delete(section)
    db.session.commit()
    return jsonify({'message': 'Section deleted successfully'})

# Social Integration endpoints
@storefront_bp.route('/storefronts/<int:storefront_id>/integrations', methods=['GET'])
def get_integrations(storefront_id):
    integrations = SocialIntegration.query.filter_by(storefront_id=storefront_id).all()
    return jsonify([integration.to_dict() for integration in integrations])

@storefront_bp.route('/storefronts/integrations/<int:integration_id>', methods=['GET'])
def get_integration(integration_id):
    integration = SocialIntegration.query.get_or_404(integration_id)
    return jsonify(integration.to_dict())

@storefront_bp.route('/storefronts/<int:storefront_id>/integrations', methods=['POST'])
def create_integration(storefront_id):
    data = request.get_json()
    
    if not data or not all(k in data for k in ('platform',)):
        return jsonify({'error': 'Missing required fields'}), 400
    
    integration = SocialIntegration(
        storefront_id=storefront_id,
        platform=data['platform'],
        account_id=data.get('account_id'),
        access_token=data.get('access_token'),
        is_active=data.get('is_active', True)
    )
    
    db.session.add(integration)
    db.session.commit()
    
    return jsonify(integration.to_dict()), 201

@storefront_bp.route('/storefronts/integrations/<int:integration_id>', methods=['PUT'])
def update_integration(integration_id):
    integration = SocialIntegration.query.get_or_404(integration_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(integration, key):
            setattr(integration, key, value)
    
    db.session.commit()
    return jsonify(integration.to_dict())

@storefront_bp.route('/storefronts/integrations/<int:integration_id>', methods=['DELETE'])
def delete_integration(integration_id):
    integration = SocialIntegration.query.get_or_404(integration_id)
    db.session.delete(integration)
    db.session.commit()
    return jsonify({'message': 'Integration deleted successfully'})
