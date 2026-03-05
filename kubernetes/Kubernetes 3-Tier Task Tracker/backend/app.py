from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Use the credentials we set in the secret
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://admin:mypassword123@mongodb-service:27017")
client = MongoClient(MONGO_URL)
db = client.task_db

# CRITICAL: This route stops the 404 errors and tells K8s the pod is healthy
@app.route('/')
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks')
def get_tasks():
    try:
        tasks = list(db.tasks.find({}, {'_id': 0}))
        return jsonify({"status": "success", "data": tasks})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
