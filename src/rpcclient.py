import xmlrpc.client
import hashlib

hash_object = hashlib.md5(b'Hello World')

def hashFunction():
    return hash_object.hexdigest()

with xmlrpc.client.ServerProxy('http://localhost:8000') as s:
    print(s.pow(2,3))  # Returns 2**3 = 8
    print(s.add(2,3))  # Returns 5
    print(s.div(5,2)) # Returns 5//2 = 2
    print(hashFunction())
    print(s.hashFunc())

# Print list of available methods
print(s.system.listMethods())
input("Press Enter to stop...")