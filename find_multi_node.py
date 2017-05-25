#!/usr/bin/env python2.7

import urllib
import requests

url = 'https://na27.salesforce.com/sfdc/multiNodeOrgs.jsp'

#info = urllib.urlopen(url)
info = requests.get(url)
#print(info.json())

for o in info


