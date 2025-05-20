from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Storefront(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    logo_url = db.Column(db.String(500))
    banner_url = db.Column(db.String(500))
    theme = db.Column(db.String(50), default='default')
    custom_domain = db.Column(db.String(255))
    is_published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'logo_url': self.logo_url,
            'banner_url': self.banner_url,
            'theme': self.theme,
            'custom_domain': self.custom_domain,
            'is_published': self.is_published,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class StorefrontSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storefront_id = db.Column(db.Integer, db.ForeignKey('storefront.id'), nullable=False)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    type = db.Column(db.String(50), nullable=False)  # hero, products, about, contact, etc.
    position = db.Column(db.Integer, default=0)
    settings = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'storefront_id': self.storefront_id,
            'title': self.title,
            'content': self.content,
            'type': self.type,
            'position': self.position,
            'settings': self.settings,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class SocialIntegration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    storefront_id = db.Column(db.Integer, db.ForeignKey('storefront.id'), nullable=False)
    platform = db.Column(db.String(50), nullable=False)  # whatsapp, instagram, facebook, etc.
    account_id = db.Column(db.String(255))
    access_token = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'storefront_id': self.storefront_id,
            'platform': self.platform,
            'account_id': self.account_id,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
