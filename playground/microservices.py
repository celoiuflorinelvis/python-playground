"""
@See: https://github.com/umermansoor/microservices
"""

from flask import Flask
from flask import request
import json


# Load sample data
with (open('data_db.json', 'r')) as f:
    data = json.load(f)


# Create flask app
app = Flask(__name__)

# Register microservices endpoints
@app.route("/users", methods=["GET"])
def get_all_users():
    return data

@app.route("/users/<userid>", methods=["GET"])
def get_user(userid):
    found_user = {}
    for user in data:
        print(f'user.id={user["id"]} / userid = {userid} / equals={int(user["id"]) == int(userid)}')
        if int(user["id"]) == int(userid):
            found_user = user
            break
    return found_user

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.get_json()
    new_id = max(user["id"] for user in data)
    new_user["id"] = int(new_id) + 1
    data.append(new_user)
    return new_user

@app.route("/users/<userid>", methods=["PUT"])
def change_user(userid):
    found_user = {}
    for user in data:
        #print(f'user.id={user["id"]} / userid = {userid} / equals={int(user["id"]) == int(userid)}')
        if int(user["id"]) == int(userid):
            mod_user = request.get_json()
            user["name"] = mod_user["name"]
            user["age"] = mod_user["age"]

            found_user = user
            break
    return found_user

@app.route("/users/<userid>", methods=["DELETE"])
def delete_user(userid):
    found_user = {}
    for user in data:
        #print(f'user.id={user["id"]} / userid = {userid} / equals={int(user["id"]) == int(userid)}')
        if int(user["id"]) == int(userid):
            data.remove(user)
            found_user = user
            break
    return found_user


# Run application
if __name__ == "__main__":
    app.run(port=5001, debug=True)
