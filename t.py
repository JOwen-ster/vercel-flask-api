import requests

data = requests.post('https://vercel-flask-api-ex.vercel.app/post?id=1&name=example')

print(data.text)