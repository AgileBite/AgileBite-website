import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Get the port number from the environment variable, defaulting to 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Run the app with the specified host and port
    app.run(host="0.0.0.0", port=port)
