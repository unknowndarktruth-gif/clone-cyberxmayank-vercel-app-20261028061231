from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
app = Flask(__name__, static_folder='..', static_url_path='')
CORS(app)
@app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_handler(path):
    return jsonify({"success": True, "path": path, "method": request.method})
@app.route('/')
def root():
    return send_from_directory('..', 'index.html')
if __name__ == '__main__':
    app.run(port=5000)
