# Import required modules from Flask
from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Route for the main page (calculator interface)
@app.route('/')
def index():
    """
    Render the main calculator page.
    Returns the index.html template which contains the calculator interface.
    """
    return render_template('index.html')

# Route for handling calculation requests
@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Handle calculation requests from the frontend.
    
    This function:
    1. Receives JSON data containing two numbers and an operation
    2. Performs the requested calculation
    3. Returns the result or an error message
    
    Expected JSON format:
    {
        "num1": number,
        "num2": number,
        "operation": "+" | "-" | "*" | "/"
    }
    
    Returns:
    - Success: JSON with result
    - Error: JSON with error message and appropriate HTTP status code
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Extract numbers and operation from the request
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']
        
        # Perform the requested calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 400
            result = num1 / num2
        else:
            # Return error for invalid operation
            return jsonify({'error': 'Invalid operation'}), 400
            
        # Return the calculation result
        return jsonify({'result': result})
        
    except (ValueError, KeyError):
        # Handle invalid input (non-numeric values or missing fields)
        return jsonify({'error': 'Invalid input'}), 400
    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application if this file is executed directly
if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True) 