from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "ambaril", "email": "ambaril77@gmail.com"},
    {"id": 2, "name": "amabagas", "email": "bagas200HP@gmail.com"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"user": users}), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next(
        (
            u for u in users if u["id"] == user_id
        ), None
    )
    if user:
        return jsonify({"users": user}), 201
    return jsonify({"Message": "Data Gak ada bjirr"})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify({"Message": "Data berhasil DIMASukkan", "user": new_user}), 202

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] == user_id]
    return jsonify({"Message": "Data dihapus"}), 2003


if __name__ == '__main__':
    app.run(debug=True)