"""
API controller for handling API requests in the Flask AI project.
"""

from flask import Blueprint, request, jsonify
from app.model.data_model import DataModel
from app.utils.helpers import validate_json, validate_email, sanitize_input, format_response

api_bp = Blueprint('api', __name__)
data_model = DataModel()

@api_bp.route('/health', methods=['POST'])
def health_check():
    return jsonify({
        "status": "success",
        "message": "API is healthy",
    }),200

@api_bp.route('/data', methods=['POST'])
def echo():
    try:
        data=request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "error": "Message field is required"
            }),400

        message=data['message']
        
        return jsonify({
            'received': message,
            'length': len(message),
            'timestamp': data_model.get_timestamp()
        }),200
    except Exception as e:
        return jsonify({
            "error": str(e)
        }),500
    
@api_bp.route('/process', methods=['POST'])
def process_text():
    try:
        data=request.get_json()
        if not data or 'text' not in data:
            return jsonify({
                "error": "Text field is required"
            }),400

        text=data['text']
        options=data.get('options',{})
        result=data_model.process_text(text,options)

        return jsonify({
            'original': text,
            'processed': result,
            'timestamp': data_model.get_timestamp()
        }),200
    except Exception as e:
        return jsonify({
            "error": str(e)
        }),500
    
@api_bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        data=request.get_json()
        if not data or 'operation' not in data or 'numbers' not in data:
            return jsonify({
                "error": "Operation and numbers fields are required"
            }),400

        operation=data['operation']
        numbers=data['numbers']
        result=data_model.calculate(operation,numbers)

        return jsonify({
            'operation': operation,
            'numbers': numbers,
            'result': result,
            'timestamp': data_model.get_timestamp()
        }),200
    except Exception as e:
        return jsonify({
            "error": f'Invalid input: {str(e)}'
        }),500
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }),500
    
    