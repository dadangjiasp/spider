from fake_useragent import UserAgent
import requests

url = 'http://www.santostang.com'
ua=UserAgent()
headers={"User-Agent":ua.random}
response=requests.get(url=url,headers=headers)

print(response.status_code)
print (response.request.headers)