import xmlrpc.client
import hashlib

hash_object = hashlib.md5(b'Hello World')

def hashFunction():
    return hash_object.hexdigest()

with xmlrpc.client.ServerProxy('http://localhost:8000') as s:
    print(hashFunction())
    print(s.hashFunc())

# Print list of available methods
print(s.system.listMethods())
input("Press Enter to stop...")