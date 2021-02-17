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

import os
import json

download_url = input("Please enter the download check URL")
conditionMet = False
while not conditionMet:
    private_key = input("Please enter location of the private key\n")
    if os.path.exists(private_key):
        conditionMet = True
    else:
        print("Invalid path given, try again.")

ignore_next_action = input("Do you want to ignore the next action?\n")
configData = {}
if ignore_next_action.lower() == "y":
    configData["ignore-next"] = True
else:
    configData["ignore-next"] = False
configData["last-id"] = "none"
configData["download"] = download_url
configData["private-key"] = private_key
configData["ignore-next"] = ignore_next_action

json_str = json.dumps(configData)
f = open('./' + "config.json", 'wb')
encrypt_bytes = bytes(json_str, encoding="utf-8")
f.write(encrypt_bytes)
f.close()

