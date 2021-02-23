************************************
Configuring Unlocke
************************************

Once the packages are installed via PIP you can now start setting up Unlocke, but before we can access to configuration
utility we need to generate a private and public key.

Navigate into the Encryptor folder and run the following
command
::
    python3 keygenerator.py

This will create a private and public key. Download the Private and Public Key and keep it in a safe place
(preferably off the server, in a secure storage solution )


Now copy the private key to the Main Script folder on the server.

Run the configurator, with the following
command
::
    python3 configurator.py

It will ask you for a download URL For an action file that the script will check every 15 minutes to see if a command
needs to be executed.

It will also ask for the location of the private key. You can reference the current directory by using ./filename

Once you go through the prompts you can proceed to the next section.



