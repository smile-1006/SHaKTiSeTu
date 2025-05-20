from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Tender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(255), nullable=False)
    reference_number = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float)
    deadline = db.Column(db.DateTime, nullable=False)
    eligibility_criteria = db.Column(db.Text)
    document_url = db.Column(db.String(500))
    status = db.Column(db.String(50), default='open')  # open, closed, awarded
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'source': self.source,
            'reference_number': self.reference_number,
            'category': self.category,
            'value': self.value,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'eligibility_criteria': self.eligibility_criteria,
            'document_url': self.document_url,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class TenderApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tender_id = db.Column(db.Integer, db.ForeignKey('tender.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50), default='draft')  # draft, submitted, under_review, accepted, rejected
    submission_date = db.Column(db.DateTime)
    documents = db.Column(db.JSON)  # JSON array of document URLs
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'tender_id': self.tender_id,
            'user_id': self.user_id,
            'status': self.status,
            'submission_date': self.submission_date.isoformat() if self.submission_date else None,
            'documents': self.documents,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
