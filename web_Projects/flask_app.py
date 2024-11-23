from flask import Flask

app = Flask(__name__)

@app.route('/home')  # Defining the route for the main page
def home():
    return "<h1> Hello, World! <h1> "  # The response for the homepage


@app.route('/path/<path>')  # Defining the route for the main page
def path(path):
    return f"This is my {path} "  # The response for the path

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=False)