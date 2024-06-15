from flask import Flask

app = Flask(__name__)

# Function to write text to the file when the application starts
def write_initial_text():
    with open('Malware Detection.txt', 'a') as file:
        file.write('Initial text written by the Flask application\n')

@app.route('/')
def home():
    return "Welcome to the Malware Detection Service!"

if __name__ == '__main__':
    # Write text to the file before starting the Flask server
    write_initial_text()
    app.run(host='0.0.0.0', port=10000, debug=False)
