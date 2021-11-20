import urllib.request
import time
# from importlib import reload
# import update as update_m

def access(url, test):# repeatly try to get the page at 10s/tries
    while True:
        try:
            page = urllib.request.urlopen(url)
            break
        except:
            if test:
                print("Fail to access " + url)
            time.sleep(10)
    return page

def update(test =False):# update all python code
    vUrl = access("https://albertlin2288.github.io/april_fool/version.txt", test)
    version = int(vUrl.read().decode().strip())
    with open("version.txt") as file:
        my_version = int(file.read().strip())
    if my_version < version:
        adUrl = access("https://albertlin2288.github.io/april_fool/address.txt", test)
        address = adUrl.read().decode().strip()
        for i in address.split("\n"):
            program_ad = access(i.split(" ")[1], test)
            with open(i.split(" ")[0], "w") as file:
                file.write(program_ad.read().decode())
        with open("version.txt", "w") as file:
            file.write(str(version))
