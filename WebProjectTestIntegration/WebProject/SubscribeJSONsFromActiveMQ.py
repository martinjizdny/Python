import json
import stomp
import time

#Subscribe JSONs from ActiveMQ
class SubscribeJSONsFromActiveMQ(object):
    def __init__(self, connection, connectionCredentials, message_count):
        self.conn = connection
        self.connectionCredentials = connectionCredentials
        self.message_count = message_count

    def on_message(self, message):
        self.message_count += 1
        print("Message No.{0} has been subscribed from ActiveMQ".format(self.message_count))
        json_data = json.loads(message.body)
        json_listX.append(json_data)
  
    def on_error(self, message):
        print("\nReceived an error {e}\n".format(e=message))

    def subscribeJSONsFromActiveMQ(self):
        global json_listX
        json_listX = []
        destination = "/queue/event" #"/topic/event" / "/queue/event" 
        #self.conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
        self.conn.set_listener('', self)
        time.sleep(1)
        #self.conn.connect(login="admin", passcode="admin", wait=True)
        self.conn.connect(self.connectionCredentials)
        self.conn.subscribe(id='simple_listener', destination=destination, ack='auto')
        print("\n***************************************************\nWaiting for messages to subscribe from ActiveMQ...")
        return json_listX  