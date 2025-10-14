from urllib.request import urlopen, Request

url = "https://www.bilibili.com"
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
req = Request(url, headers=headers)
resp = urlopen(req)

with open("mybili.html",mode="w") as f: 
  f.write(resp.read().decode("utf-8"))
print("运行完成")