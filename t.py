import requests

data = requests.get('https://vercel-flask-api-ex.vercel.app/post?id=1&name=example')

print(data.text)