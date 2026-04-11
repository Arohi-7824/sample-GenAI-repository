"""
Helper Functions for the Flask AI Project
"""

import re
from functools import wraps
from flask import request, jsonify

def validate_json(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400
            
            data = request.get_json()
            missing_fields=[]

            for field in required_fields:
                if field not in data:
                    missing_fields.append(field)

            if missing_fields:
                return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_input(text):
    text=re.sub(r'[^\w\s]', '', text)
    text=' '.join(text.split())
    return text.strip()

def format_response(data, status=200):
    response={
        "status": "success" if status == 200 else "error",
        "data": data
    }
    if message:
        response["message"]=message
    return message