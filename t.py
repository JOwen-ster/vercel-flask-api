import requests

base_url = 'https://vercel-flask-api-ex.vercel.app'

get_resp = requests.get(base_url+'/api/get')
post_resp = requests.post(base_url+'/post?id=1&name=example')
delete_resp = requests.delete(base_url+'/api/delete?id=1')

print(get_resp.text)
print(post_resp.text)
print(delete_resp.text)