import requests, re
ptype = "socks.txt" #socks.txt for socks, proxy.txt for http
regex = r"([0-9]+(?:\.[0-9]+){3}:[0-9]+).*\+"
regex_cleaner = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
c = requests.get("https://spys.me/" + ptype)
test_str = c.text
a = re.finditer(regex, test_str, re.MULTILINE)
with open("proxies_list.txt", 'w') as file:
    for i in a:
       print(i.group(1),file=file)



