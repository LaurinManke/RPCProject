import xmlrpc.client
import hashlib

hash_object = hashlib.md5(b'Hello World')

def hashFunction():
    return hash_object.hexdigest()

with xmlrpc.client.ServerProxy('http://localhost:8000') as s:
    random_number_client = (s.rnd())
    print(random_number_client)
    print(hashFunction())
    print(s.hashFunc())
    print(s.rnd())

# Print list of available methods
print(s.system.listMethods())
input("Press Enter to stop...")