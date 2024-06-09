from djitellopy import Tello
import paho.mqtt.client as mqtt
import time 

# Teste utilizando o broker mosquitto
Broker = 'test.mosquitto.org'
Topic = 'testeTelloMqtt'
Port = 1883

# Criando um cliente MQTT
client = mqtt.Client()
client.connect(Broker, Port)

# Conectando-se ao tello
tello = Tello()
tello.connect()

while True:
    # Obtendo dados dos sensores
    state = tello.get_current_state()

    # Publicando no tópico
    client.publish(Topic, str(state))

    time.sleep(1)





