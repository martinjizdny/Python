import json
import csv
import pandas as pd

#save JSON to csv file
def saveJsonToCsvFile(json_list):
    print("\n***************************************************\nSaving the JSONs to the csv file(s)")
    item_count = 0
    for item in json_list:  
        json_dict = json.loads(item)

        #Convert the data types and structure
        transformed_json_list = []
        for item in json_dict['list']:
            transformed_json_item = {
                'id': int(item['id']),
                'firstName': item['firstName'],
                'lastName': item['lastName'],
                'streetName': item['address']['streetName'],
                'postCode': int(item['address']['postCode']),
                'cityName': item['address']['cityName'],
                'countryCode': item['address']['countryCode'],
                'isPostBox': item['address']['isPostBox'].lower() == 'true',
                'addressLine1': item['addressLine1'],
                'country': item['country'],
                'phoneNumber': item.get('phoneNumber', None),
                'cellularPhoneNumber': item.get('cellularPhoneNumber', None),
                'emailAddress': item['emailAddress'],
                'dateOfBirth': item['dateOfBirth'],
                'hasSecretAddress': item['hasSecretAddress'].lower() == 'true',
                'isReservedAgainstSalesMaterial': item['isReservedAgainstSalesMaterial'].lower() == 'true'
            }
            transformed_json_list.append(transformed_json_item)

        modified_json_list = json.dumps(transformed_json_list)

        python_object_list = json.loads(modified_json_list) #parse a JSON string into a Python object            
        python_object_list_values = [list(item.values()) for item in python_object_list] #Extract values without keys

        #adding 'list' at the beginning
        for item_python in python_object_list_values: 
            item_python.insert(0, "list")
                       
        #Modify the CSV dialect to use semicolon delimiter
        csv.register_dialect('mydialect', delimiter=';')
        
        #Write the values to the CSV file
        file_name = "C:\\TEMP\\Output_file{}.csv".format(item_count)
        with open(file_name, 'w', newline='') as csvfile: 
            writer = csv.writer(csvfile, dialect='mydialect')
            writer.writerows(python_object_list_values)
            print("The \"{}\" saved".format(file_name))

        item_count += 1        

    #Convert JSON data to DataFrame and save to CSV (the whole unformatted CSV) - OPTIONAL!!!
    df = pd.DataFrame(json_list)
    file_name = "C:\\TEMP\\Output_file.csv"
    df.to_csv(file_name, index=False)
    print("The \"{}\" saved".format(file_name))