# Control Flrig from python - test of possibilities

import time
import xmlrpc.client

CTCSS = {
    "67.0":"000","69.3":"001","71.9":"002","74.4":"003","77.0":"004","79.7":"005","82.5":"006","85.4":"007","88.5":"008","91.5":"009","94.8":"010","97.4":"011","100.0":"012","103.5":"013","107.2":"014","110.9":"015","114.8":"016","118.8":"017","123.0":"018","127.3":"019","131.8":"020","136.5":"021","141.3":"022","146.2":"023","151.4":"024","156.7":"025","159.8":"026","162.2":"027","165.5":"028","167.9":"029","171.3":"030","173.8":"031","177.3":"032","179.9":"033","183.5":"034","186.2":"035","189.9":"036","192.8":"037","196.6":"038","199.5":"039","203.5":"040","206.5":"041","210.7":"042","218.1":"043","225.7":"044","229.1":"045","233.6":"046","241.8":"047","250.3":"048","254.1":"049"
} #CTCSS table for FT891
from operator import itemgetter
#print([key for key in CTCSS.keys()][25])
#print([value for value in CTCSS.values()][25])


ServerURL = "http://localhost:12345" # Flrig address

with xmlrpc.client.ServerProxy(ServerURL) as proxy:
    #print("freq: %s" % str(proxy.rig.list_methods()))
    #print("info: %s" % str(proxy.rig.get_info()))
    #proxy.rig.set_vfo(float(26835000)) # or proxy.main.set_frequency(float(3756000))
    #print("freq: %s" % str(proxy.rig.get_vfo()))

    # CB FM hotspot
    #proxy.rig.set_vfo(float(26835000))
    proxy.rig.set_vfo(float(26755000))
    print(proxy.rig.set_mode("FM"))
    proxy.rig.set_power(4)
    #print("Power: %s" % str(proxy.rig.get_power()))
    
    #CTCSS 0:“OFF” 1:"ENC/DEC" 2:"ENC"
    proxy.rig.cat_string("CT01;") #"ENC/DEC"
    print(proxy.rig.cat_string("CT0;")) # returns string
    #CTCSS set CN(command)+0(fixed)+0(CTCSS)+000-049(table)+;(end)
    proxy.rig.cat_string("CN00" + CTCSS["103.5"] + ";")
    print(proxy.rig.cat_string("CN00;")) # returns string



    # SCAN FREQUENCY RANGE
    #for x in range(3500000, 3800001,100):
    #for x in range(7000000, 7200001,200):
    #    proxy.main.set_frequency(float(x))
    #    time.sleep(0.2)
    #    print("freq: %s" % str(proxy.rig.get_vfo()) + " S: %s" % str(proxy.rig.get_smeter()))
        






    
