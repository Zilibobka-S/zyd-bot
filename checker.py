import time
import requests
#TODO: speed-check, smth with cookies
timeout = 5
a = 0
proxy_list = []
proxies={"http": "http://127.0.0.1:1111/", "https": "http://127.0.0.1:1111/"}


with open("proxies_list.txt", "r") as f:
    for line in f:
        proxy_list.append(line.rstrip("\n"))

print("array created")
#print(proxy_list)
for proxy in proxy_list:
    proxies["http"] = proxy
    proxies["https"] = proxy
    try:
        r = requests.get('https://youtu.be/QLBRYAPRBy4?', proxies=proxies, timeout=timeout)
        print(r.status_code)
        #print(r.text)
        print(proxy)
    except Exception:
        print("инсульт жопы")
        print(proxy)
        time.sleep(0)
print("Поппа")

