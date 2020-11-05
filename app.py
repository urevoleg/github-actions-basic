from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<div style="border:solid green 2px; padding: 20px"> <b>It's the best apps</b><br>👍</div>"""

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9876, threaded=True)