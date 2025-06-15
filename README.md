# vercel-flask-api

- Need to add request.get_json() to access JSON data in the body as another way to get data if the data is NOT being passed as a query in the url

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

- Need to add templates to render site so the site has a frontend and an api
```python
from flask import Flask, redirect, url_for, render_template

# Our Flask app object
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')

@app.route('/')
@app.route('/home')
def index():
    """Our default routes of '/' and '/home'

    Return: landing page
    """

    return render_template('index.html')
```

https://www.youtube.com/watch?v=jQjjqEjZK58
