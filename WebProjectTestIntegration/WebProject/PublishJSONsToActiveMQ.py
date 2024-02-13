import time
import json
import stomp
#from pprint import pprint

#publish JSONs to ActiveMQ
def publishJSONsToActiveMQ(global_json_data_1st, global_json_data_2nd, connection, connectionCredentials):
    message_count = 1
    
    print("\n***************************************************\nPublishing messages with JSONs to ActiveMQ")
    #connection = stomp.Connection(host_and_ports=[("localhost", 61613)])
    #connection.connect(login="admin", passcode="admin")
    connection.connect(connectionCredentials)
    
    # Ensures that the CONNECTED frame is received otherwise, the disconnect call will fail.
    time.sleep(1) 
    destination = "/queue/event" #"/topic/event" / "/queue/event" 
    
    #send JSON
    connection.send(destination, json.dumps(global_json_data_1st), persistent='true')
    print("Message No.{0} with JSON has been published to ActiveMQ".format(message_count))
    
    #send JSON
    message_count += 1
    connection.send(destination, json.dumps(global_json_data_2nd), persistent='true')
    print("Message No.{0} with JSON has been published to ActiveMQ".format(message_count))

    connection.disconnect()