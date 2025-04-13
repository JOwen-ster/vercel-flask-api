from flask import Flask, request, jsonify
app = Flask(__name__)

db = {
    1: 'user_name_1',
    2: 'user_name_2',
    3: 'user_name_3',
}

# default GET
@app.route('/')
def home():
    return jsonify('index')


@app.route('/post', methods=['POST'])
def post_user():
    data = request.get_json()  # Get JSON body of the request

    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'error': 'Missing "id" or "name" in JSON body'}), 400

    user_id = data['id']
    name = data['name']

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': '"id" must be an integer'}), 400

    db[user_id] = name

    return jsonify({'message': f'User "{name}" added with ID {user_id}'})


@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()  # Get JSON body of the request
    if not data or 'id' not in data:
        return jsonify({'error': 'Missing user ID in JSON body'}), 400

    user_id = data['id']

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': 'Invalid ID format'}), 400

    if user_id in db:
        deleted_user = db.pop(user_id)
        return jsonify({'message': f'User "{deleted_user}" deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
