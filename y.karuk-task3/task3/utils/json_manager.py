import json

class DataJson:
    '''function to extract data from json and return value'''
    def finding_value_from_json(file_name, data_key):
        with open(file_name) as f:
            data = json.load(f)
        for key, value in data.items():
            if key == data_key:
                parameter = value
            else:
                pass
        return parameter