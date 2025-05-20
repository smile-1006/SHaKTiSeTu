from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expertise = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    years_experience = db.Column(db.Integer)
    hourly_rate = db.Column(db.Float)
    availability = db.Column(db.JSON)  # JSON object with availability slots
    languages = db.Column(db.JSON)  # JSON array of languages spoken
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'expertise': self.expertise,
            'bio': self.bio,
            'years_experience': self.years_experience,
            'hourly_rate': self.hourly_rate,
            'availability': self.availability,
            'languages': self.languages,
            'is_verified': self.is_verified,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class MentorSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'), nullable=False)
    mentee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    session_type = db.Column(db.String(50), nullable=False)  # one_on_one, group, workshop
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='scheduled')  # scheduled, in_progress, completed, cancelled
    meeting_link = db.Column(db.String(500))
    recording_url = db.Column(db.String(500))
    feedback_rating = db.Column(db.Integer)
    feedback_comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'mentor_id': self.mentor_id,
            'mentee_id': self.mentee_id,
            'title': self.title,
            'description': self.description,
            'session_type': self.session_type,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'status': self.status,
            'meeting_link': self.meeting_link,
            'recording_url': self.recording_url,
            'feedback_rating': self.feedback_rating,
            'feedback_comment': self.feedback_comment,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class PeerGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100), nullable=False)
    whatsapp_link = db.Column(db.String(500))
    max_members = db.Column(db.Integer, default=100)
    is_private = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'whatsapp_link': self.whatsapp_link,
            'max_members': self.max_members,
            'is_private': self.is_private,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class PeerGroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('peer_group.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(50), default='member')  # admin, moderator, member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'user_id': self.user_id,
            'role': self.role,
            'joined_at': self.joined_at.isoformat()
        }
