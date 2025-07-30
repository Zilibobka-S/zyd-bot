
#from spys import me, one, filters, proxy_view

import time
import requests
#TODO: speed-filtering, smth with cookies
timeout = 5
a = 0
proxy_list = []
proxies={"http": "http://127.0.0.1:1111/", "https": "http://127.0.0.1:1111/"}
good_proxies = []

with open("proxies_list.txt", "r") as f:
    for line in f:
        proxy_list.append(line.rstrip("\n"))

print("array created")
#print(proxy_list)
for proxy in proxy_list:
    proxies["http"] = proxy
    proxies["https"] = proxy
    try:
        r = requests.get('https://youtu.be/YLhpPghyIQw?si=yKdGR5cTSYvLtlIL', proxies=proxies, timeout=timeout)
        print(r.status_code)
        #print(r.text)
        print(proxy)
        if r.status_code == 200:
            starttime = time.monotonic()
            rmb = requests.get('https://gist.githubusercontent.com/khaykov/a6105154becce4c0530da38e723c2330/raw/41ab415ac41c93a198f7da5b47d604956157c5c3/gistfile1.txt', proxies=proxies)
            proxytime = (time.monotonic() - starttime)
            print(proxytime)
            if proxytime < 5:
                good_proxies.append(proxy)
            else:
                print("Bad proxy, bad!")
    except Exception:
        print("инсульт жопы")
        print(proxy)
        time.sleep(0)
print("Поппа")
print(good_proxies)
