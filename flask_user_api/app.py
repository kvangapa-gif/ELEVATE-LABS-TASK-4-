from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "KUNDAN", "email": "vangapandukundan@example.com", "age": 19},
    {"id": 2, "name": "SAI", "email": "sai@example.com", "age": 20},
    {"id": 3, "name": "RAM GOPAL VARMA", "email": "ramgopalvarma@example.com", "age": 21}
]

def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data or 'age' not in data:
        return jsonify({"error": "Missing fields"}), 400
    
    new_id = max([u["id"] for u in users]) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    if 'age' in data:
        user['age'] = data['age']
    
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users.remove(user)
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)