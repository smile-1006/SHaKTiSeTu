from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)
    author = db.Column(db.String(100))
    category = db.Column(db.String(100), nullable=False)  # industry, success_story, investor
    image_url = db.Column(db.String(500))
    published_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_featured = db.Column(db.Boolean, default=False)
    tags = db.Column(db.JSON)  # JSON array of tags
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'summary': self.summary,
            'author': self.author,
            'category': self.category,
            'image_url': self.image_url,
            'published_date': self.published_date.isoformat(),
            'is_featured': self.is_featured,
            'tags': self.tags,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class SuccessStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    business_name = db.Column(db.String(255))
    industry = db.Column(db.String(100))
    challenges = db.Column(db.Text)
    solutions = db.Column(db.Text)
    results = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    video_url = db.Column(db.String(500))
    is_approved = db.Column(db.Boolean, default=False)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'content': self.content,
            'business_name': self.business_name,
            'industry': self.industry,
            'challenges': self.challenges,
            'solutions': self.solutions,
            'results': self.results,
            'image_url': self.image_url,
            'video_url': self.video_url,
            'is_approved': self.is_approved,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(100))  # angel, vc, government, etc.
    focus_areas = db.Column(db.JSON)  # JSON array of focus industries
    investment_range = db.Column(db.String(100))  # e.g., "₹10L - ₹50L"
    website_url = db.Column(db.String(500))
    logo_url = db.Column(db.String(500))
    contact_email = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'focus_areas': self.focus_areas,
            'investment_range': self.investment_range,
            'website_url': self.website_url,
            'logo_url': self.logo_url,
            'contact_email': self.contact_email,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
