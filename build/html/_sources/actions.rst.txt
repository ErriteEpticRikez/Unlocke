************************************
Creating Action Files
************************************
Action files are an encrypted file that is checked by Unlocke to determine if an action needs to be ran.

These types of files can be created by the generate_action script.py within the Encryptor folder.

.. note::   The script will require the public key. Make sure the public key is inside the directory.

To start execute the generate_action.py script using the following
command
::
    python3 keygenerator.py

It will ask you what command you want to be ran, include all the necessary arguments.

Once the .action file is created. You will need to upload it to the webserver that you set on the configurator.
Then wait 15-20 minutes for the script to detect the new action.

.. note::   Note if your webserver uses any caching such as Sucuri, Cloudflare, or Squid. You may have to clear the cache.



Executing Commands that require a confirmation
**********************************************

Some commands will require a yes input to be processed. Depending on the command, it may already have a parameter to
automatically confirm a prompt.

If the command in question does not have that parameter you will need to use the yes
command in conjunction with the command you need to
use
::
    yes | command

