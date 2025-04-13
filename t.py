import requests

data = requests.get('https://vercel-flask-api-ex.vercel.app')

print(data.text)