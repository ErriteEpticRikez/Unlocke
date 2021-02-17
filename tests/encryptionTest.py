import pytest
# unit test case
import unittest
from nacl.public import PublicKey, PrivateKey, SealedBox

class TestStringMethods(unittest.TestCase):
    # test function to test the array param creation process
    def test_array(self):
        # Generate Bob's private key, as we've done in the Box example
        private = PrivateKey.generate()
        public = private.public_key

        private_bytes = bytes(private)
        public_bytes = bytes(public)

        f = open('./private.key', 'wb')
        f.write(private_bytes)
        f.close()

        f = open('./public.key', 'wb')
        f.write(public_bytes)
        f.close()
        with open("./private.key", "rb") as f:
            priv_byte = f.read()
            with open("./public.key", "rb") as pubf:
                pubf_byte = pubf.read()
                public_key = PublicKey(pubf_byte)
                private_key = PrivateKey(priv_byte)
                test_message = "This a test message!"
                sealed_box = SealedBox(public_key)
                encrypted_text = sealed_box.encrypt(bytes(test_message, "utf-8"))
                unseal = SealedBox(private_key)

                result = unseal.decrypt(encrypted_text)
                print(result.decode("utf-8"))
                self.assertEqual(result.decode("utf-8"),test_message)


if __name__ == '__main__':
    unittest.main()
