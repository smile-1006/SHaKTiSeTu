from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class FinancialProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    business_type = db.Column(db.String(100))  # sole proprietorship, partnership, etc.
    annual_revenue = db.Column(db.Float)
    years_in_business = db.Column(db.Integer)
    credit_score = db.Column(db.Float)
    has_existing_loans = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'business_type': self.business_type,
            'annual_revenue': self.annual_revenue,
            'years_in_business': self.years_in_business,
            'credit_score': self.credit_score,
            'has_existing_loans': self.has_existing_loans,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    term_months = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, approved, rejected, disbursed
    interest_rate = db.Column(db.Float)
    documents = db.Column(db.JSON)  # JSON array of document URLs
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'purpose': self.purpose,
            'term_months': self.term_months,
            'status': self.status,
            'interest_rate': self.interest_rate,
            'documents': self.documents,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ShippingProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    api_key = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ShipmentOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('shipping_provider.id'), nullable=False)
    tracking_number = db.Column(db.String(100))
    status = db.Column(db.String(50), default='pending')  # pending, in_transit, delivered, failed
    shipping_cost = db.Column(db.Float)
    estimated_delivery = db.Column(db.DateTime)
    actual_delivery = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'provider_id': self.provider_id,
            'tracking_number': self.tracking_number,
            'status': self.status,
            'shipping_cost': self.shipping_cost,
            'estimated_delivery': self.estimated_delivery.isoformat() if self.estimated_delivery else None,
            'actual_delivery': self.actual_delivery.isoformat() if self.actual_delivery else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
