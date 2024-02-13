import requests
import json

def getJsonsFromWebAndFile():    
    print("\n***************************************************\nGetting JSONs from Web and file")
    from requests.auth import HTTPBasicAuth #https://docs.python-requests.org/en/latest/user/authentication/
    basic = HTTPBasicAuth('user', 'pass')
    #response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    response.raise_for_status()  #check for errors
    print("Request status = {}".format(response.status_code))
    global global_json_data_1st
    global global_json_data_2nd
    global_json_data_1st = json.loads(response.text) #Load JSON data into a Python variable.
    #global_json_data_2nd = "Hello world"

    # Reading JSON data from a file
    with open("C:\\Users\\jizdnmar\\Downloads\\!RestAPI\\Output_file_AMQ.json") as f:
        global_json_data_2nd = json.load(f)
        global_json_data_1st = global_json_data_2nd

    print("All the JSONs files imported")
    return global_json_data_1st, global_json_data_2nd