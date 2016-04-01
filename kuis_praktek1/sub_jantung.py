import paho.mqtt.client as mqtt

mqttc = mqtt.Client('sub2', clean_session=False)


def on_message(mqttc, obj, msg):
    print "Topik: " + msg.topic + " message" + msg.payload

mqttc.on_message = on_message

# make connection to broker
mqttc.connect("127.0.0.1", 1883)

# subscribe
mqttc.subscribe("rumahsakit/poli/jantung")

# serve in forever loop
mqttc.loop_forever()