# Import the Flask Dependency
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/') # forward slash indicates we're putting our data at the root of our route

def hello_world():
    return 'Did this work?'