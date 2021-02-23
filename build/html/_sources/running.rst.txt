***************
Running Unlocke
***************

There are two ways that you can run Unlocke, you can either do it via a SystemD service or run it under tmux/screen.

Service / Unit File
*******************
To create a custom systemd service you need to create a unit file.

Make sure to fill in the required fields (User, Group, and the path to the script/main.py)
Unit file here
::
    [Unit]
    Description=Unlocke
    Documentation=https://github.com/ErriteEpticRikez/Unlocke
    Wants=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user here>
    Group=<user group here>
    ExecReload=/bin/kill -HUP $MAINPID
    ExecStart=python3 /pathtomainscript
    SyslogIdentifier=Unlocke
    Restart=always

    [Install]
    WantedBy=multi-user.target

Tmux / Screen
*******************
If you only want to run it under certain situations. You can run it under a tmux or screen session. Once you have
opened a session run the following command
::
    python3 /path to main.py
