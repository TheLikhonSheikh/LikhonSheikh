# Get the current price of Bitcoin in USD using the coindesk.com API with Python and the Requests HTTP library

import requests # http://docs.python-requests.org/en/master/

btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

#print(btc.status_code)
#print(btc.headers['content-type'])
#print(btc.encoding)
#print(btc.text)

print(btc.json()['bpi']['USD']['rate'])
