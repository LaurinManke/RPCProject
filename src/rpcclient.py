import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:8000') as s:
    print(s.pow(2,3))  # Returns 2**3 = 8
    print(s.add(2,3))  # Returns 5
    print(s.div(5,2)) # Returns 5//2 = 2

# Print list of available methods
print(s.system.listMethods())
input("Press Enter to stop...")