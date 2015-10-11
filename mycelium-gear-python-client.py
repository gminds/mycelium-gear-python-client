import hmac
import time
import base64
import hashlib
import urllib2

host = 'gateway.gear.mycelium.com'
gateway_id = '6930af63a087cad5cd920e12e4729fe4f777681cb5b92cbd9a021376c0f91930'
secret = '5ioHLiVwxqkS6Hfdev8pNQfhA9xy7dK957RBVYycMhfet23BTuGUPbYxA9TP6x9P'
body = ''

nonce = int(round(time.time() * 1000))
nonce_body_hash = hashlib.sha512(unicode(nonce) + unicode(body))

path = '/gateways/{}/orders?amount=1&keychain_id=1'.format(gateway_id)
request = "POST" + path + nonce_body_hash.digest()
full_request = "https://{}{}".format(host, path)

signature_hmac = hmac.new(secret, request, hashlib.sha512)
signature = base64.b64encode(signature_hmac.digest())

headers = {'X-Nonce': nonce, 'X-Signature': signature}
post_data = {}

r = urllib2.Request(full_request, post_data, headers=headers)
contents = urllib2.urlopen(r).read()
print contents
