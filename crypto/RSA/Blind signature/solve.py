from pwn import *
import json as js
from Crypto.Util.number import *

conn = remote("socket.cryptohack.org", 13376)
conn.recvuntil(b"\n")

get_pubkey = {
	"option": "get_pubkey"
}
conn.sendline(js.dumps(get_pubkey).encode())
pubkey = js.loads(conn.recvuntil(b"\n")[:-1].decode())
pubkey["N"], pubkey["e"] = int(pubkey["N"], 16), int(pubkey["e"], 16)

ADMIN_TOKEN = bytes_to_long(b"admin=True")
k = pow(2, pubkey["e"], pubkey["N"])
msg = long_to_bytes(k * ADMIN_TOKEN).hex()
sign = {
	"option": "sign",
	"msg": msg
}
conn.sendline(js.dumps(sign).encode())
signature = js.loads(conn.recvuntil(b"\n")[:-1].decode())
signature["signature"] = int(signature["signature"], 16)
adminTokenSign = (signature["signature"] * inverse(2, pubkey["N"])) % pubkey["N"]

verify = {
	"option": "verify",
	"msg": b"admin=True".hex(),
	"signature": hex(adminTokenSign)
}
conn.sendline(js.dumps(verify).encode())
print(conn.recvuntil(b"\n")[:-1].decode())