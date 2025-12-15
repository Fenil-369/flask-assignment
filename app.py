import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data_from_file():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        print(data)    
        return jsonify(data)
    
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)