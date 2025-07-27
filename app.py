from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Clean Flask App!"

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"}), 200

@app.route('/run', methods=['POST'])
def run_command():
    data = request.get_json()
    cmd = data.get('cmd')
    if not cmd or not cmd.isalpha():
        return jsonify({"error": "Invalid or dangerous input"}), 400

    try:
        result = subprocess.run(["echo", cmd], capture_output=True, text=True, check=True)
        return jsonify({"output": result.stdout}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
