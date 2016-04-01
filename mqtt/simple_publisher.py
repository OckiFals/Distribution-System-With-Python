import paho.mqtt.client as mqtt

# MQTT client initialization
mqttc = mqtt.Client('publ1', clean_session=False)

# make connection to broker
mqttc.connect("127.0.0.1", 1883)

# publish message
mqttc.publish("filkom/sister/b", payload="Selamat Pagi", qos=1, retain=False)