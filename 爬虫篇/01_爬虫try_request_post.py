import requests

url = "https://fanyi.baidu.com/v2transapi"


response = requests.post(url, data="a")
# response = response.content.decode()
print(response)
