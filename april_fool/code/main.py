from time import localtime
from update import update
update()
t=list(localtime())
if t[1:3] == [4,1]:
    pass
else:
    import selfprotect
    selfprotect.main()
