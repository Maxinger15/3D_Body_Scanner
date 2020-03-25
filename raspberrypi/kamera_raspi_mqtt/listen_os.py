import paho.mqtt.client as mqtt
import socket
import subprocess
import shutil
import os
import glob
import logging
from datetime import datetime

#First: pip3 install paho-mqtt
print("Starte Listener")
name = socket.gethostname()


def on_connect2(client, userdata, flags, rc):
    client.subscribe("scanner",2)
    print("Connected "+str(rc))
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Recived message: "+str(msg.payload,'UTF-8'))
    
    if(str(msg.payload,'UTF-8') == "shoot"):
        cmd = ("raspistill --encoding png --timeout 1 -o /home/pi/pic/"+name+"_"+str(datetime.now().strftime("%d_%m_%Y_T_%H_%M_%S"))+".png")
        subprocess.call(cmd, shell=True)
        client.publish("scanner_status",qos=2,payload=socket.gethostname()+"_Finished Shot")
    if(str(msg.payload,'UTF-8') == "copy"):
        for filename in glob.glob(os.path.join("/home/pi/pic", '*.*')):
            shutil.copy(filename, "/mnt/gx1/fotos")
            os.remove(filename)
        client.publish("scanner_status",qos=2,payload=socket.gethostname()+"_Copied Files")

client = mqtt.Client()

logger = logging.getLogger(__name__)
client.enable_logger(logger)

client.on_connect = on_connect2
client.on_message = on_message


client.connect("gx1", 1883,60)
client.loop_forever()




