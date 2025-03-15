from flask import Blueprint, jsonify,request
from app.models import User
from flask_jwt_extended import create_access_token
from app.schemas import user_schema

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/',methods=['POST'])
def login():
    data = request.get_json()
    # Validate input
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400

    # Find user by email
    user = User.query.filter_by(email=data['email']).first()
    if not user or (data['password']):  
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user.email))
    return jsonify({
        'message': 'Logged in successfully',
        'token' : access_token,
        'user': user_schema.dump(user)
    })