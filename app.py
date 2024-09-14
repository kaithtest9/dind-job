from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/run-docker')
def run_docker():
    output = subprocess.run(['docker', 'run', 'hello-world'], capture_output=True)
    stdout = output.stdout.decode('utf-8')
    stderr = output.stderr.decode('utf-8')
    return jsonify({
        'stdout': stdout,
        'stderr': stderr
    })

if __name__ == '__main__':
    app.run(debug=True)