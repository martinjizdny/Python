import stomp
import time
import CallApiManager
import PublishJSONsToActiveMQ
import SaveJsonToCsvFile
import SubscribeJSONsFromActiveMQ
import sys
from StartListening import FlaskAPI
from pprint import pprint


# ************* MAIN *************
#connectionListening = stomp.Connection(host_and_ports=[("localhost", 5555)])
connectionListening = ["localhost", "5555"]
connectionActiveMQ = stomp.Connection(host_and_ports=[("localhost", 61613)])
connectionActiveMQCredentials = ("admin", "admin")

#OPTIONAL - CSV from file:
#global_json_data_1st = {}
#global_json_data_2nd = {}
#global_json_data_1st, global_json_data_2nd = CallApiManager.getJsonsFromWebAndFile()
#PublishJSONsToActiveMQ.publishJSONsToActiveMQ(global_json_data_1st, global_json_data_2nd)


#Start listening ...
flask_app = FlaskAPI(connectionListening)
json_data = flask_app.run_flask_app()

#Publish JSONs to ActiveMQ
PublishJSONsToActiveMQ.publishJSONsToActiveMQ(json_data, json_data, connectionActiveMQ, connectionActiveMQCredentials)

#Subscribe JSONs from ActiveMQ
subscriber_instance = SubscribeJSONsFromActiveMQ.SubscribeJSONsFromActiveMQ(connectionActiveMQ, connectionActiveMQCredentials, 0)
json_list = subscriber_instance.subscribeJSONsFromActiveMQ()

#Save JSONs to csv file(s)
time.sleep(1)
SaveJsonToCsvFile.saveJsonToCsvFile(json_list)

print("\n***************************************************\n\nAnd that's it!")
sys.exit()