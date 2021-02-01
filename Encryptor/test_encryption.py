
from nacl.public import PublicKey, PrivateKey, SealedBox

with open("./private.key", "rb") as f:
    priv_byte = f.read()
    with open("./public.key", "rb") as pubf:
        pubf_byte = pubf.read()
        public_key = PublicKey(pubf_byte)
        private_key = PrivateKey(priv_byte)
        test_message = "This a test message!"
        sealed_box = SealedBox(public_key)
        encrypted_text = sealed_box.encrypt(bytes(test_message,"utf-8"))
        unseal = SealedBox(private_key)

        result = unseal.decrypt(encrypted_text)
        print(result.decode("utf-8"))
