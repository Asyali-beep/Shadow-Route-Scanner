from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/public/status', methods=['GET'])
def status():
    return jsonify({"status": "running", "version": "1.0"}), 200

@app.route('/api/secure/data', methods=['GET'])
def secure_data():
    return jsonify({"error": "Unauthorized Access"}), 401

@app.route('/api/internal/backup', methods=['GET'])
def secret_backup():
    return jsonify({"file": "database.sql.gz", "size": "1.5GB", "status": "download_ready"}), 200

@app.route('/api/dev/debug', methods=['GET'])
def debug_info():
    return jsonify({"db_user": "root", "db_pass": "123456", "env": "production"}), 200

if __name__ == '__main__':
    app.run(port=5000)