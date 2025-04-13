from flask import Flask, request, jsonify
app = Flask(__name__)


db = {
    1 : 'user_name_1',
    2 : 'user_name_2',
    3 : 'user_name_3',
    
}

# default GET
@app.route('/')
def home():
    return jsonify('index')


@app.route('/post', methods=['POST'])
def post_user():
    # # /post?id=1&name='example'
    user_id = request.args.get('id')
    name = request.args.get('name')

    # json of all args
    data = request.get_json()
    print(data)

    if not user_id or not name:
        return jsonify({'error': 'Missing "id" or "name" in query parameters'}), 400

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': '"id" must be an integer'}), 400

    db[user_id] = name

    return jsonify({'message': f'User "{name}" added with ID {user_id}'})


@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.args.get('id')
    if not data:
        return jsonify({'error': 'Missing user ID'}), 400

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': 'Invalid ID format'}), 400

    if user_id in db:
        deleted_user = db.pop(user_id)
        return jsonify({'message': f'User "{deleted_user}" deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
