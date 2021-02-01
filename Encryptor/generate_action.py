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
import uuid
import json
from nacl.public import PublicKey, PrivateKey, SealedBox

with open("./public.key", "rb") as pubf:
    pubf_byte = pubf.read()
    public_key = PublicKey(pubf_byte)
    input_command = input("Please input the desired command\n")
    action_list = {}
    action_list["action"] = input_command
    action_list["id"] = str(uuid.uuid4())
    json_str = json.dumps(action_list)
    print(json_str)
    sealed_box = SealedBox(public_key)
    encrypted_text = sealed_box.encrypt(bytes(json_str,"utf-8"))
    file_name = input("Please input what you want the action file to be called.\n")
    f = open('./' + file_name, 'wb')
    encrypt_bytes = bytes(encrypted_text)
    f.write(encrypt_bytes)
    f.close()
