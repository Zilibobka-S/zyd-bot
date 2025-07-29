from io import StringIO
import time
import requests
a = 0
proxy_list = []
with open("proxies_list.txt", "r") as f:
    for line in f:
        proxy_list.append(line.rstrip("\n"))
print("array created")
for proxy in proxy_list:
    a = (a+1)
    print(a)


