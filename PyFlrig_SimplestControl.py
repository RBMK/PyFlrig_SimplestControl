import time
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:12345") as proxy:
    #print("freq: %s" % str(proxy.rig.list_methods()))
    #print("info: %s" % str(proxy.rig.get_info()))
    #proxy.main.set_frequency(float(3756000))
    #print("freq: %s" % str(proxy.rig.get_vfo()))



    

    # SCAN FREQUENCY RANGE    
    #for x in range(3500000, 3800001,100):
    for x in range(7000000, 7200001,100):
        proxy.main.set_frequency(float(x))
        time.sleep(0.1)
        print("freq: %s" % str(proxy.rig.get_vfo()))
