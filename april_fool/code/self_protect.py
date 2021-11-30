import time
import os
import atexit
path = r"D:\New folder\\"
short_path = os.getenv("appdata")+r"\Microsoft\Windows\Start Menu\Programs" +\
             r"\Startup\start.lnk"
def write(files={}):
    try:
        with open(r"D:\New folder\stop.txt") as file:
            if file.read() == "Password":
                print("Password right")
                return None
    except:pass
    print("Wrong password or no password")
    os.makedirs(path, exist_ok = True)
    try:#try to install SWinLnk and then create shortcut.
        from swinlnk.swinlnk import SWinLnk
        swl=SWinLnk()
        swl.create_lnk(path+"start.cmd", short_path)
        print("Successfully recreated shortcut")
    except:
        for i in range(10):
            try:
                os.system("py -m pip install swinlnk")
                from swinlnk.swinlnk import SWinLnk
                swl=SWinLnk()
                swl.create_lnk(path+"start.cmd", short_path)
                print("Successfully recreated shortcut")
                break
            except:pass
    for i in files:
        with open(path+i,"w") as file:
            file.write(files[i])
            print("Writing file", path+i)
atexit.register(write)
def main():
    files={}
    for i in os.scandir("D:\\New folder"):
        if os.path.isfile(os.path.join("D:\\New folder",i)):
            with open(i) as file:
                files[i.name] = file.read()
                print("Reading file",path+i.name)
    while 1:
        try:
            time.sleep(int(0.5*60))
        except:
            write(files)
            break
        write(files)

if __name__ == "__main__":
    main()
