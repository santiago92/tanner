
import requests
import json
import logging
import http.client as http_client

HOST = "192.168.100.167"
PORT = "12201"



class Graylog:

    def __init__(self):
        self.endpoint = "http://"+HOST+":"+PORT+"/gelf"
        logging.info ('init graylog endpoint {0}'.format(self.endpoint))

    def http_log(arg):
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    def send_data(self,data):
    	print('url for post {}, data {}'.format(self.endpoint,data))
        http_log()
    	requests.post(self.endpoint, json={'short_message':'test_graylogs'})
