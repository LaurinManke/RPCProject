from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import hashlib
import random

hash_object_server = hashlib.md5(b'Hello World')
random_number_server = float
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

def randomFunction():
    random_number_server = random.random()
    return random_number_server
server.register_function(randomFunction, 'rnd')

def hashFunction():
    return hash_object_server.hexdigest()
server.register_function(hashFunction, 'hashFunc')

print("Server is listening on port 8000...")

# Run the server's main loop
server.serve_forever()

