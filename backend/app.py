from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os, sys, time

app = Flask(__name__)
CORS(app)

# Read connection string from env
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/bankdb")
# Wait-for-mongo simple retry
max_tries = 10
for i in range(max_tries):
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        client.server_info()  # raise if cannot connect
        break
    except Exception as e:
        if i == max_tries - 1:
            print("Cannot connect to MongoDB:", e, file=sys.stderr)
            raise
        time.sleep(2)

db = client.get_database()  # uses DB from URI
users = db.get_collection("users")
accounts = db.get_collection("accounts")

@app.route("/")
def hello():
    return jsonify({"msg": "Bank API running"})

@app.route("/register", methods=["POST"])
def register():
    data = request.json or {}
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "username/password required"}), 400
    if users.find_one({"username": data["username"]}):
        return jsonify({"error": "user exists"}), 400
    users.insert_one({"username": data["username"], "password": data["password"]})
    accounts.insert_one({"username": data["username"], "balance": 1000.0})
    return jsonify({"msg": "registered"}), 201

@app.route("/accounts/<username>", methods=["GET"])
def get_accounts(username):
    acc = list(accounts.find({"username": username}, {"_id": 0}))
    return jsonify(acc)

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json or {}
    from_user = data.get("from")
    to_user = data.get("to")
    try:
        amount = float(data.get("amount", 0))
    except:
        return jsonify({"error": "invalid amount"}), 400

    if amount <= 0:
        return jsonify({"error": "invalid amount"}), 400

    from_acc = accounts.find_one({"username": from_user})
    to_acc = accounts.find_one({"username": to_user})

    if not from_acc or not to_acc:
        return jsonify({"error": "account not found"}), 404
    if from_acc["balance"] < amount:
        return jsonify({"error": "insufficient funds"}), 400

    accounts.update_one({"username": from_user}, {"$inc": {"balance": -amount}})
    accounts.update_one({"username": to_user}, {"$inc": {"balance": amount}})
    return jsonify({"msg": "transfer successful"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
