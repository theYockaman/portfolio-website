from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    """User model for authentication."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    

class Project(db.Model):
    """Model for storing project information."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    demo_url = db.Column(db.String(500))
    technologies = db.Column(db.Text)  # Stored as comma-separated values
    featured = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())


class ContactMessage(db.Model):
    """Model for storing contact form submissions."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())


class Skill(db.Model):
    """Model for storing skills and proficiency levels."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, default=50)  # 0-100
    category = db.Column(db.String(50))  # e.g., 'Programming', 'Framework', 'Tool'
    order = db.Column(db.Integer, default=0)


class Experience(db.Model):
    """Model for storing work experience."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    description = db.Column(db.Text)
    order = db.Column(db.Integer, default=0)
