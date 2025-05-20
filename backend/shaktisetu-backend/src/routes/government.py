from flask import Blueprint, jsonify, request
from src.models.government import GovernmentScheme, SchemeApplication
from src.models.user import db

government_bp = Blueprint('government', __name__)

# Government Scheme endpoints
@government_bp.route('/schemes', methods=['GET'])
def get_schemes():
    schemes = GovernmentScheme.query.filter_by(is_active=True).all()
    return jsonify([scheme.to_dict() for scheme in schemes])

@government_bp.route('/schemes/<int:scheme_id>', methods=['GET'])
def get_scheme(scheme_id):
    scheme = GovernmentScheme.query.get_or_404(scheme_id)
    return jsonify(scheme.to_dict())

@government_bp.route('/schemes', methods=['POST'])
def create_scheme():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'description')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    scheme = GovernmentScheme(
        name=data['name'],
        description=data['description'],
        ministry=data.get('ministry'),
        eligibility_criteria=data.get('eligibility_criteria'),
        benefits=data.get('benefits'),
        application_process=data.get('application_process'),
        documents_required=data.get('documents_required'),
        deadline=data.get('deadline'),
        website_url=data.get('website_url'),
        contact_info=data.get('contact_info'),
        is_active=data.get('is_active', True)
    )
    
    db.session.add(scheme)
    db.session.commit()
    
    return jsonify(scheme.to_dict()), 201

@government_bp.route('/schemes/<int:scheme_id>', methods=['PUT'])
def update_scheme(scheme_id):
    scheme = GovernmentScheme.query.get_or_404(scheme_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(scheme, key):
            setattr(scheme, key, value)
    
    db.session.commit()
    return jsonify(scheme.to_dict())

# Scheme Application endpoints
@government_bp.route('/schemes/<int:scheme_id>/applications', methods=['GET'])
def get_scheme_applications(scheme_id):
    applications = SchemeApplication.query.filter_by(scheme_id=scheme_id).all()
    return jsonify([app.to_dict() for app in applications])

@government_bp.route('/users/<int:user_id>/applications', methods=['GET'])
def get_user_applications(user_id):
    applications = SchemeApplication.query.filter_by(user_id=user_id).all()
    return jsonify([app.to_dict() for app in applications])

@government_bp.route('/schemes/<int:scheme_id>/applications', methods=['POST'])
def create_application(scheme_id):
    data = request.get_json()
    
    if not data or not all(k in data for k in ('user_id',)):
        return jsonify({'error': 'Missing required fields'}), 400
    
    application = SchemeApplication(
        scheme_id=scheme_id,
        user_id=data['user_id'],
        status=data.get('status', 'draft'),
        submission_date=data.get('submission_date'),
        documents=data.get('documents'),
        notes=data.get('notes')
    )
    
    db.session.add(application)
    db.session.commit()
    
    return jsonify(application.to_dict()), 201

@government_bp.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    application = SchemeApplication.query.get_or_404(application_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(application, key):
            setattr(application, key, value)
    
    db.session.commit()
    return jsonify(application.to_dict())

@government_bp.route('/schemes/check-eligibility', methods=['POST'])
def check_eligibility():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('user_id', 'scheme_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # This would typically involve more complex logic to check eligibility
    # For now, we'll just return a placeholder response
    return jsonify({
        'eligible': True,
        'message': 'You are eligible for this scheme',
        'missing_documents': []
    })
