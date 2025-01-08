import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_tea():
    return "Hello, Tea! This is a minimal Python project."

if __name__ == '__main__':
    app.run(debug=True)
  
