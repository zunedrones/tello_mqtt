from djitellopy import Tello
import paho.mqtt.client as mqtt
import time 

# Teste utilizando o broker mosquitto
Broker = 'test.mosquitto.org'
Topic = 'testeTelloMqtt'
Port = 1883

# Função chamada quando o subscriber recebe uma mensagem
def on_message(client, userdata, message):
    print("Mensagem recebida:", str(message.payload.decode("utf-8")))

# Criando um cliente MQTT
client = mqtt.Client()

# Associando a função on_message à recepção de mensagens
client.on_message = on_message

# Conectando-se ao broker
client.connect(Broker, Port)

# Inscrevendo-se no tópico "teste"
client.subscribe(Topic)

# Loop para receber mensagens
client.loop_forever()

