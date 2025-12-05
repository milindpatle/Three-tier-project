# In your app.py, update the MongoDB connection:
import os
from pymongo import MongoClient

# Use Kubernetes service name
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongodb-service:27017/bankdb")
# OR if using headless service
# MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongodb-0.mongodb-headless.default.svc.cluster.local:27017/bankdb")

# Add health endpoint
@app.route('/health')
def health():
    try:
        client.server_info()
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500