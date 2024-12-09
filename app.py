from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Route to handle form submission
@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # Extract form data
        form_data = {
            "name": request.form.get('name', ''),
            "email": request.form.get('email', ''),
            "message": request.form.get('message', '')
        }

        # Debugging: Print form data to console
        print("Form Data:", form_data)

        # Path to the submissions JSON file
        submissions_file = 'submissions.json'

        # Load existing submissions or initialize an empty list
        if os.path.exists(submissions_file):
            with open(submissions_file, 'r') as f:
                submissions = json.load(f)
        else:
            submissions = []

        # Append new data and write to JSON file
        submissions.append(form_data)
        with open(submissions_file, 'w') as f:
            json.dump(submissions, f, indent=4)

        return jsonify({"message": "Form submitted successfully!", "status": "success"}), 200

    except Exception as e:
        print(f"Error processing form: {e}")
        return jsonify({"message": "Failed to submit the form.", "status": "error"}), 500

# Root route for basic testing
@app.route('/')
def index():
    return '''
    <h1>Flask Form Submission</h1>
    <p>Submit your form at <code>/submit-form</code>.</p>
    '''

if __name__ == '__main__':
    # Run on localhost with debug mode
    app.run(debug=True)
