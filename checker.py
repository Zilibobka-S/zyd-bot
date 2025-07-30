
#from spys import me, one, filters, proxy_view
import asyncio
import time
import httpx
#TODO: speed-check, smth with cookies
timeout = 5
a = 0
realstart = time.monotonic()
longurl = 'https://gist.githubusercontent.com/khaykov/a6105154becce4c0530da38e723c2330/raw/41ab415ac41c93a198f7da5b47d604956157c5c3/gistfile1.txt' #i dont wanna waste ur time with a lot of letters
proxy_list = []
good_proxy = []
async def multithread():
    tasks = [proxytester(proxy) for proxy in proxy_list]
    good_proxy = await asyncio.gather(*tasks)
    print(good_proxy)

async def proxytester(proxy):
    async with httpx.AsyncClient(proxy=proxy) as client:
        async with asyncio.Semaphore(10):
            r = await client.get('https://www.youtube.com/watch?v=YLhpPghyIQw', timeout=timeout)
            #print(r.status_code)
            #print(proxy)
            start_time = time.monotonic()
            rd = await client.get(longurl)
            processtime = time.monotonic() - start_time
            #print(processtime)
            if (r.status_code == 200) and (processtime < 60):
                return ("aw tysm")
            else:
                return("бля не робит")




with open("proxies_list.txt", "r") as f: #txt file -> array
    for line in f:
        line = ("http://" + line)
        proxy_list.append(line.rstrip("\n"))


print("array created")
print(proxy_list)
#for proxy in proxy_list:
try:
    asyncio.run(multithread())

#        r = httpx.get('https://youtu.be/YLhpPghyIQw', proxies=proxies, timeout=timeout)
#        print(r.status_code)
#        #print(r.text)
#        print(proxy)

except Exception as error:
    print(error)
    print("инсульт жопы")

    time.sleep(0)
print("Поппа")
print(time.monotonic() - realstart)
print(good_proxy)
