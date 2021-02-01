
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
import json
from nacl.public import PrivateKey, SealedBox

with open("./private.key", "rb") as f:
    with open("./test.action", "rb") as actionF:

        priv_byte = f.read()
        action_byte = actionF.read()
        private_key = PrivateKey(priv_byte)
        test_message = "This a test message!"
        sealed_box = SealedBox(private_key)
        encrypted_text = sealed_box.decrypt(action_byte)
        results = json.loads(encrypted_text.decode("utf-8"))
        print(results)
