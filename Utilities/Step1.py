import json
import urllib2

# product_JSON
products = { "items" : [
    { "itemId":1,"itemName":"item1","itemAmount":20},
    { "itemId":2,"itemName":"item2","itemAmount":40}
]}

req = urllib2.Request('http://localhost:22236/registerTransaction/merchant1')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(products))

print response.read()