"""
    Unlocke

    Copyright (C) 2020  Errite Games LLC/ ErriteEpticRikez
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import nacl.utils
from nacl.public import PrivateKey, SealedBox, PublicKey

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





print("Test")