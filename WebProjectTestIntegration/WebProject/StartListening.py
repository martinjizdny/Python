import json
import xml.etree.ElementTree as ET
import threading
import stomp
from flask import Flask, request, jsonify

class FlaskAPI:
    def __init__(self, connection):
        self.app = Flask(__name__)
        self.global_json_data = None
        self.global_json_data_lock = threading.Lock()
        self.connectionHost = connection[0]
        self.connectionPort = connection[1]
        print("\n***************************************************\nStart waiting for POST request ... ")

        #@app.route('/helloWorld', methods=['POST'])
        #def hello_world():
        #    return "Hello World !!!"

        @self.app.route('/pythonTest', methods=['POST'])
        def parse_xml():
            global global_json_data
            if request.method == 'POST':
                xml_authorization = request.authorization
                xml_data = request.data
                root = ET.fromstring(xml_data)        
        
                #Find the soapenv:Body with actor
                body_actor = root.find('.//actor')
        
                data_dict = {} 
                #Iterate through the actor's list elements and populate the dictionary
                for list_element in body_actor.findall('.//list'):
                    record = {}
                    for element in list_element:
                        record[element.tag] = element.text
                        if element.findall('.//*'):
                            nested_dict = {}
                            for nested_element in element:
                                nested_dict[nested_element.tag] = nested_element.text
                            record[element.tag] = nested_dict
                    data_dict[list_element.tag] = data_dict.get(list_element.tag, []) + [record]

                self.global_json_data = json.dumps(data_dict, indent=2)

                #Use a lock to safely update the shared variable
                with self.global_json_data_lock:
                    self.global_json_data = self.global_json_data

                return jsonify(self.global_json_data)

    def listen_from_api_manager(self):
        #self.app.run(host="localhost", port=5555)
        self.app.run(host=self.connectionHost, port=self.connectionPort)
    
    def run_flask_app(self):
        #Create a thread for the Flask application
        flask_thread = threading.Thread(target=self.listen_from_api_manager)
        flask_thread.start()

        #Wait for the POST request to be received and processed
        while True:
            with self.global_json_data_lock:
                if self.global_json_data is not None:
                    break

        print("POST request received and processed!\n")
        return self.global_json_data

if __name__ == "__main__":
    flask_app = FlaskAPI()
    flask_app.run_flask_app()
