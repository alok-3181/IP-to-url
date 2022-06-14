import requests
import sys
import os
import time
import urllib3
urllib3.disable_warnings()
with open('urls.txt') as f:
    for content in f:
        time.sleep(4)
        content = content.strip('\n')
        content = content.strip('\t')   
        url = "http://" + content
        
        response = requests.get(url, allow_redirects=True, verify=False, timeout=10)
        if response.history:
            for resp in response.history:
                print response.url
            else:
                print url
        response.close()
