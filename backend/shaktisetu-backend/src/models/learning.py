from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)  # beginner, intermediate, advanced
    language = db.Column(db.String(50), nullable=False)  # english, hindi, tamil, etc.
    duration_minutes = db.Column(db.Integer)
    thumbnail_url = db.Column(db.String(500))
    is_published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'level': self.level,
            'language': self.language,
            'duration_minutes': self.duration_minutes,
            'thumbnail_url': self.thumbnail_url,
            'is_published': self.is_published,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class CourseModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    position = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'position': self.position,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class CourseLesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('course_module.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)  # video, audio, text
    content_url = db.Column(db.String(500))
    content_text = db.Column(db.Text)
    duration_minutes = db.Column(db.Integer)
    position = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'module_id': self.module_id,
            'title': self.title,
            'content_type': self.content_type,
            'content_url': self.content_url,
            'content_text': self.content_text,
            'duration_minutes': self.duration_minutes,
            'position': self.position,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class UserCourseProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('course_lesson.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    progress_percentage = db.Column(db.Float, default=0)
    last_position = db.Column(db.Float, default=0)  # For video/audio, position in seconds
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'lesson_id': self.lesson_id,
            'completed': self.completed,
            'progress_percentage': self.progress_percentage,
            'last_position': self.last_position,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
