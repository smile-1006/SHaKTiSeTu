from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    full_name = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    business_name = db.Column(db.String(200))
    business_type = db.Column(db.String(100))
    role = db.Column(db.String(50), default='seller')  # admin, seller, buyer, mentor
    profile_image = db.Column(db.String(500))
    preferred_language = db.Column(db.String(50), default='english')
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'phone': self.phone,
            'business_name': self.business_name,
            'business_type': self.business_type,
            'role': self.role,
            'profile_image': self.profile_image,
            'preferred_language': self.preferred_language,
            'is_verified': self.is_verified,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
