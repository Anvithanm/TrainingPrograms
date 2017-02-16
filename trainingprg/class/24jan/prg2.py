import requests as r
import json
g = r.get("http://122.181.186.42:9200/anvitha")
#print g.text
json_str = g.text
#print json_str
#json_dict = json.dumps(json_str, indent=5)
#print json_dict
print json_str['anvitha']['settings']['index']['uuid']
