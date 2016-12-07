
import requests
import json
import logging as log

HOST = "192.168.100.167"
PORT = "12201"
URL = "http://:12201/gelf"


class Graylog:

    def __init__(self):
        self.endpoint = "http://"+HOST+":"+PORT+"/gelf"
        log.info ('init graylog endpoint {0}'.format(self.endpoint))

    def send_data(self,data):
    	print('url for post {}, data {}'.format(self.endpoint,data))
    	#requests.post(self.endpoint, data=json.dumps(data))





