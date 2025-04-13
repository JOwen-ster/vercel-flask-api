from flask import Flask, request, jsonify
app = Flask(__name__)


db = {
    1: 'user_name_1',
    2: 'user_name_2',
    3: 'user_name_3',
}

# defaults to GET method if methods are not specified
@app.route('/')
@app.route('/index')
def index():
    return jsonify({'content':'index'})


@app.route('/api/get', methods=['GET'])
def get():
    return jsonify({'content':'hello world'})


@app.route('/api/post', methods=['POST'])
def post():
    # Get query parameters
    # # /post?id=1&name=example
    user_id = request.args.get('id')
    name = request.args.get('name')

    # Check if the parameters are provided
    if not user_id or not name:
        return jsonify({'error': 'Missing "id" or "name" in query parameters'}), 400

    try:
        user_id = int(user_id)  # Ensure the id is an integer
    except ValueError:
        return jsonify({'error': '"id" must be an integer'}), 400

    # Add to the database
    db[user_id] = name

    return jsonify({'content': f'User "{name}" added with ID {user_id}'})


@app.route('/api/delete', methods=['DELETE'])
def delete():
    data = request.args.get('id')
    if not data:
        return jsonify({'error': 'Missing user ID'}), 400

    try:
        user_id = int(data)
    except ValueError:
        return jsonify({'error': 'Invalid ID format'}), 400

    if user_id in db:
        deleted_user = db.pop(user_id)
        print(deleted_user)
        return jsonify({'content': f'User "{deleted_user}" deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
