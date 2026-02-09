
# Flask Imports
from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect
from .data import get_config_manager
from .models import ContactMessage, Project
from . import db

# Views Blueprint
views = Blueprint('views', __name__)

# Get configuration manager
config = get_config_manager()


# Home Route
@views.route('/', methods=['GET', 'POST'])
def home():
    """Render the home page with configuration data."""
    return render_template(
        "index.html",
        config=config.get(),
        hero=config.get('hero'),
        projects=config.get('projects', [])
    )


# About Route
@views.route('/about', methods=['GET'])
def about():
    """Render the about page."""
    return render_template(
        "about.html",
        config=config.get(),
        about=config.get('about'),
        personal=config.get('personal')
    )


# Projects Route
@views.route('/projects', methods=['GET'])
def projects():
    """Render the projects page."""
    return render_template(
        "projects.html",
        config=config.get(),
        projects=config.get('projects', [])
    )


# Contact Route
@views.route('/contact', methods=['GET', 'POST'])
def contact():
    """Render the contact page and handle form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject', '')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('Please fill in all required fields.', 'error')
        else:
            try:
                # Save to database
                new_message = ContactMessage(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                db.session.add(new_message)
                db.session.commit()
                flash('Thank you for your message! I will get back to you soon.', 'success')
                return redirect(url_for('views.contact'))
            except Exception as e:
                flash('An error occurred. Please try again later.', 'error')
                print(f"Error saving contact message: {e}")
    
    return render_template(
        "contact.html",
        config=config.get(),
        contact_info=config.get('contact'),
        personal=config.get('personal')
    )


# Shop Route
@views.route('/shop', methods=['GET'])
def shop():
    """Render the shop page."""
    return render_template(
        "shop.html",
        config=config.get()
    )


# API endpoint to get configuration
@views.route('/api/config', methods=['GET'])
def get_config():
    """API endpoint to retrieve configuration data."""
    return jsonify(config.get())


# API endpoint for contact form (if using AJAX)
@views.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint for contact form submissions."""
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'email', 'message')):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    
    try:
        new_message = ContactMessage(
            name=data['name'],
            email=data['email'],
            subject=data.get('subject', ''),
            message=data['message']
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Message sent successfully'})
    except Exception as e:
        print(f"Error saving contact message: {e}")
        return jsonify({'success': False, 'message': 'Server error'}), 500

