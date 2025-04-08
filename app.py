
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "My name is Likhil Penujuli"

if __name__ == '__main__':
    app.run()
