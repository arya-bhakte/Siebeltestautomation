from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import os
app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS for React frontend

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        
        # Server-side validation
        errors = {}
        
        # Validate name
        if not data.get('name', '').strip():
            errors['name'] = 'Name is required'
        elif len(data.get('name', '')) > 100:
            errors['name'] = 'Name cannot exceed 100 characters'
            
        # Validate case name
        if not data.get('caseName', '').strip():
            errors['caseName'] = 'Case Name is required'
        elif len(data.get('caseName', '')) > 100:
            errors['caseName'] = 'Case Name cannot exceed 100 characters'
            
        # Validate description
        if not data.get('description', '').strip():
            errors['description'] = 'Description is required'
        elif len(data.get('description', '')) > 250:
            errors['description'] = 'Description cannot exceed 250 characters'
        
        if errors:
            return jsonify({'success': False, 'errors': errors}), 400
        
        # If validation passes, you can process the data here
        # For now, we'll just print it and return success
        print("Form submitted successfully:")
        print(f"Name: {data['name']}")
        print(f"Case Name: {data['caseName']}")
        print(f"Description: {data['description']}")
        
        return jsonify({
            'success': True, 
            'message': 'Form submitted successfully!',
            'data': data
        })
        
    except Exception as e:
        return jsonify({'success': False, 'errors': {'general': str(e)}}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)