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
import urllib3
import time
import json
import os
import shutil
import subprocess
from nacl.public import PrivateKey, SealedBox
from errite.arraytools.parameterMaker import makeParameterArray

print("Unlocke Main Component V1.0")
configData = None
doContinue = True
if os.path.exists("./config.json"):
    with open("./config.json", "r") as jsonFile:
        configData = json.load(jsonFile)
elif not os.path.exists("./config.json"):
    print("Warning! Config file is mpt present, use configurator to create a config file. ")
    doContinue = False
if doContinue:
    noError = True
    try:
        c = urllib3.PoolManager()
        url = configData["download"]
        with open("./private.key", "rb") as f:
            while noError:
                with c.request('GET', url, preload_content=False) as resp, open("main.action", 'wb') as out_file:
                    shutil.copyfileobj(resp, out_file)
                resp.release_conn()
                with open("./main.action", "rb") as actionF:
                    priv_byte = f.read()
                    action_byte = actionF.read()
                    private_key = PrivateKey(priv_byte)
                    test_message = "This a test message!"
                    sealed_box = SealedBox(private_key)
                    encrypted_text = sealed_box.decrypt(action_byte)
                    results = json.loads(encrypted_text.decode("utf-8"))
                    cmd = results["action"]
                    cmd_array = makeParameterArray(cmd)
                    main_cmd = cmd_array[0]
                    if configData["ignore-next"].lower() == "y":
                        configData["last-id"] = results["id"]
                        json_str = json.dumps(configData)
                        f = open('./' + "config.json", 'wb')
                        encrypt_bytes = bytes(json_str, encoding="utf-8")
                        f.write(encrypt_bytes)
                        f.close()
                        os.remove("./main.action")
                    elif not configData["last-id"] == results["id"]:
                        end_len:int = len(cmd_array)
                        subprocess.run(cmd, shell=True)
                        configData["last-id"] = results["id"]
                        json_str = json.dumps(configData)
                        f = open('./' + "config.json", 'wb')
                        encrypt_bytes = bytes(json_str, encoding="utf-8")
                        f.write(encrypt_bytes)
                        f.close()
                        os.remove("./main.action")
                    time.sleep(900)
    except Exception as ex:
        noError = False
        print("Exiting from application due to hit exception! " + ex.args[0])
