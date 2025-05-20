from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class GovernmentScheme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ministry = db.Column(db.String(255))
    eligibility_criteria = db.Column(db.Text)
    benefits = db.Column(db.Text)
    application_process = db.Column(db.Text)
    documents_required = db.Column(db.JSON)  # JSON array of required documents
    deadline = db.Column(db.DateTime)
    website_url = db.Column(db.String(500))
    contact_info = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'ministry': self.ministry,
            'eligibility_criteria': self.eligibility_criteria,
            'benefits': self.benefits,
            'application_process': self.application_process,
            'documents_required': self.documents_required,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'website_url': self.website_url,
            'contact_info': self.contact_info,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class SchemeApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scheme_id = db.Column(db.Integer, db.ForeignKey('government_scheme.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50), default='draft')  # draft, submitted, under_review, approved, rejected
    submission_date = db.Column(db.DateTime)
    documents = db.Column(db.JSON)  # JSON array of document URLs
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'scheme_id': self.scheme_id,
            'user_id': self.user_id,
            'status': self.status,
            'submission_date': self.submission_date.isoformat() if self.submission_date else None,
            'documents': self.documents,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
