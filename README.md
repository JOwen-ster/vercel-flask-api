# vercel-flask-api

- Need to add get_json as another way to get data if the data is NOT being passed as a query in the url

```python
@app.route('/post', methods=['POST'])
def post_user():
    data = request.get_json()  # Access JSON data in the body
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'error': 'Missing "id" or "name" in JSON body'}), 400

    user_id = data['id']
    name = data['name']
    # Handle the data...
    return jsonify({'message': f'User "{name}" added with ID {user_id}'})
```