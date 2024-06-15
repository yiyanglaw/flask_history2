from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to write initial text to the file when the application starts
def write_initial_text():
    with open('Malware Detection.txt', 'a') as file:
        file.write('Initial text written by the Flask application\n')

# Route to write any text to the file
@app.route('/write/<text>', methods=['GET'])
def write_text(text):
    with open('Malware Detection.txt', 'a') as file:
        file.write(text + '\n')
    return jsonify({"message": f"Text '{text}' written to Malware Detection.txt"}), 200

# Route to display the contents of the file
@app.route('/display', methods=['GET'])
def display_text():
    try:
        with open('Malware Detection.txt', 'r') as file:
            content = file.read()
        return jsonify({"content": content}), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/')
def home():
    return "Welcome to the Malware Detection Service!"

if __name__ == '__main__':
    # Write text to the file before starting the Flask server
    write_initial_text()
    app.run(host='0.0.0.0', port=10000, debug=False)
