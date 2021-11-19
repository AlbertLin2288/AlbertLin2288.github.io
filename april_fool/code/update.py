import urllib.request
import time

def access(url):# repeatly try to get the page at 10s/tries
    while True:
        try:
            page = urllib.request.urlopen(url)
            break
        except:
            time.sleep(10)
    return page

base = "https://albertlin2288.github.io/april_fool/address.txt"
def update():
    webUrl = access(base)
    address = webUrl.read().decode().strip()
    for i in address.split("\n"):
        program_ad = access(i.split(" ")[1])
        with open(i.split(" ")[0], "w") as file:
            file.write(program_ad.read().decode())
