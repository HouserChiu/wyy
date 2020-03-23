import requests

headers = {
    'referer': 'https://music.163.com/user/home?id=50359783',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

url = 'https://music.163.com/user/home?id=50359783'

response = requests.get(url, headers=headers)
print(response.text)