from flask import Blueprint, jsonify, request
from src.models.mentorship import Mentor, MentorSession, PeerGroup, PeerGroupMember
from src.models.user import db

mentorship_bp = Blueprint('mentorship', __name__)

# Mentor endpoints
@mentorship_bp.route('/mentors', methods=['GET'])
def get_mentors():
    mentors = Mentor.query.filter_by(is_verified=True).all()
    return jsonify([mentor.to_dict() for mentor in mentors])

@mentorship_bp.route('/mentors/<int:mentor_id>', methods=['GET'])
def get_mentor(mentor_id):
    mentor = Mentor.query.get_or_404(mentor_id)
    return jsonify(mentor.to_dict())

@mentorship_bp.route('/mentors', methods=['POST'])
def create_mentor():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('user_id', 'expertise', 'bio')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    mentor = Mentor(
        user_id=data['user_id'],
        expertise=data['expertise'],
        bio=data['bio'],
        years_experience=data.get('years_experience'),
        hourly_rate=data.get('hourly_rate'),
        availability=data.get('availability'),
        languages=data.get('languages'),
        is_verified=data.get('is_verified', False)
    )
    
    db.session.add(mentor)
    db.session.commit()
    
    return jsonify(mentor.to_dict()), 201

@mentorship_bp.route('/mentors/<int:mentor_id>', methods=['PUT'])
def update_mentor(mentor_id):
    mentor = Mentor.query.get_or_404(mentor_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(mentor, key):
            setattr(mentor, key, value)
    
    db.session.commit()
    return jsonify(mentor.to_dict())

# Mentor Session endpoints
@mentorship_bp.route('/sessions', methods=['GET'])
def get_sessions():
    sessions = MentorSession.query.all()
    return jsonify([session.to_dict() for session in sessions])

@mentorship_bp.route('/mentors/<int:mentor_id>/sessions', methods=['GET'])
def get_mentor_sessions(mentor_id):
    sessions = MentorSession.query.filter_by(mentor_id=mentor_id).all()
    return jsonify([session.to_dict() for session in sessions])

@mentorship_bp.route('/users/<int:user_id>/mentee-sessions', methods=['GET'])
def get_mentee_sessions(user_id):
    sessions = MentorSession.query.filter_by(mentee_id=user_id).all()
    return jsonify([session.to_dict() for session in sessions])

@mentorship_bp.route('/sessions', methods=['POST'])
def create_session():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('mentor_id', 'mentee_id', 'title', 'session_type', 'start_time', 'end_time')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    session = MentorSession(
        mentor_id=data['mentor_id'],
        mentee_id=data['mentee_id'],
        title=data['title'],
        description=data.get('description'),
        session_type=data['session_type'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        status=data.get('status', 'scheduled'),
        meeting_link=data.get('meeting_link')
    )
    
    db.session.add(session)
    db.session.commit()
    
    return jsonify(session.to_dict()), 201

@mentorship_bp.route('/sessions/<int:session_id>', methods=['PUT'])
def update_session(session_id):
    session = MentorSession.query.get_or_404(session_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(session, key):
            setattr(session, key, value)
    
    db.session.commit()
    return jsonify(session.to_dict())

# Peer Group endpoints
@mentorship_bp.route('/peer-groups', methods=['GET'])
def get_peer_groups():
    groups = PeerGroup.query.filter_by(is_private=False).all()
    return jsonify([group.to_dict() for group in groups])

@mentorship_bp.route('/peer-groups/<int:group_id>', methods=['GET'])
def get_peer_group(group_id):
    group = PeerGroup.query.get_or_404(group_id)
    return jsonify(group.to_dict())

@mentorship_bp.route('/peer-groups', methods=['POST'])
def create_peer_group():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'category', 'created_by')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    group = PeerGroup(
        name=data['name'],
        description=data.get('description'),
        category=data['category'],
        whatsapp_link=data.get('whatsapp_link'),
        max_members=data.get('max_members', 100),
        is_private=data.get('is_private', False),
        created_by=data['created_by']
    )
    
    db.session.add(group)
    db.session.commit()
    
    # Add creator as admin member
    member = PeerGroupMember(
        group_id=group.id,
        user_id=data['created_by'],
        role='admin'
    )
    
    db.session.add(member)
    db.session.commit()
    
    return jsonify(group.to_dict()), 201

@mentorship_bp.route('/peer-groups/<int:group_id>/members', methods=['GET'])
def get_group_members(group_id):
    members = PeerGroupMember.query.filter_by(group_id=group_id).all()
    return jsonify([member.to_dict() for member in members])

@mentorship_bp.route('/peer-groups/<int:group_id>/join', methods=['POST'])
def join_group(group_id):
    data = request.get_json()
    
    if not data or not data.get('user_id'):
        return jsonify({'error': 'User ID is required'}), 400
    
    # Check if user is already a member
    existing_member = PeerGroupMember.query.filter_by(group_id=group_id, user_id=data['user_id']).first()
    if existing_member:
        return jsonify({'error': 'User is already a member of this group'}), 400
    
    member = PeerGroupMember(
        group_id=group_id,
        user_id=data['user_id'],
        role=data.get('role', 'member')
    )
    
    db.session.add(member)
    db.session.commit()
    
    return jsonify(member.to_dict()), 201
