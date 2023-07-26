from test_onoff import SystemOnOff
from test_rasp2ino import Rasp2Ino
from test_record import Record

#systemonoff 
#touchin 12 out 4 charger 18
n = input("1-touch 2-chrger 3-r2a 4-record")

if n ==1 :
    a = -1 
    a = SystemOnOff.Touch()
    print (a)

elif n == 2:
    a = -1 
    a = SystemOnOff.BeeConnect()
    print (a)
    
elif n==3 :
    inputnum = input("arduino")
    Rasp2Ino.send_number_to_arduino(inputnum)

elif n==4 :
    lis = Record.store()
    print (lis)