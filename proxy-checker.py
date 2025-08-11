

#from spys import me, one, filters, proxy_view
import proxies
import json
import time
import requests
#TODO: speed-filtering, smth with cookies
timeout = 3
a = 0
proxy_list = []
proxies_http={"http": "http://127.0.0.1:1111/", "https": "http://127.0.0.1:1111/"}
good_proxies = {}

proxies.get_proxy()



startreal = time.monotonic()
with open("proxies_list.txt", "r") as f:
    for line in f:
        proxy_list.append(line.rstrip("\n"))

print("array created")
#print(proxy_list)
for proxy in proxy_list:
    proxies_http["http"] = proxy
    proxies_http["https"] = proxy
    try:
        r = requests.get('https://youtu.be/YLhpPghyIQw?si=yKdGR5cTSYvLtlIL', proxies=proxies_http, timeout=timeout)
        print(r.status_code)
        #print(r.text)
        print(proxy)
        if r.status_code == 200:
            starttime = time.monotonic()
            rmb = requests.get('https://gist.githubusercontent.com/khaykov/a6105154becce4c0530da38e723c2330/raw/41ab415ac41c93a198f7da5b47d604956157c5c3/gistfile1.txt', proxies=proxies_http, timeout=5)
            proxytime = (time.monotonic() - starttime)
            print(proxytime)
            if proxytime < 5:
                good_proxies[proxy] = proxytime
                print("Found good proxy!")
            else:
                print("Bad proxy, bad!")
    except Exception:
        print("инсульт жопы")
        print(proxy)
        time.sleep(0)
sorted_proxies = dict(sorted(good_proxies.items(), key=lambda item: item[1], reverse=True))
print("Поппа")
print(good_proxies)
print(time.monotonic() - startreal)
print (sorted_proxies)
with open ("good_proxies.json", "w") as f:
    json.dump(sorted_proxies, f, indent=2)
