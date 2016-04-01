import json
import paho.mqtt.client as mqtt
from SimpleXMLRPCServer import SimpleXMLRPCServer

# MQTT client initialization
mqttc = mqtt.Client('publ1', clean_session=False)

# make connection to broker
mqttc.connect("127.0.0.1", 1883)

data_pasien = [
    {
        'nik': 1,
        'nama': 'ocki',
        'alamat': 'kp pasir limus',
        'penyakit': 'maag',
        'poli': 1
    }
]


def tambahdatapasien(json_data):
    data_baru = json.loads(json_data)
    data_pasien.append(
        data_baru
    )

    if data_baru['poli'] == 1:
        mqttc.publish("rumahsakit/poli/umum", payload=json_data, qos=1, retain=False)
    elif data_baru['poli'] == 2:
        mqttc.publish("rumahsakit/poli/jantung", payload=json_data, qos=1, retain=False)
    elif data_baru['poli'] == 3:
        mqttc.publish("rumahsakit/poli/paru", payload=json_data, qos=1, retain=False)

    return 'Data berhasil disimpan'


def bacadatapasien(json_data):
    pasien = None
    nik = json.loads(json_data)['nik']
    for p in data_pasien:
        if p['nik'] == nik:
            pasien = p
            break

    if pasien is not None:
        return json.dumps(pasien)
    else:
        return 'Data Tidak Ditemukan'

server = SimpleXMLRPCServer(('', 6666))
server.register_function(tambahdatapasien, 'tambahdata')
server.register_function(bacadatapasien, 'bacadata')

server.serve_forever()