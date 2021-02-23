************************************
Installing required packages
************************************
Unlocke requires Python3 to run as well as dependencies

Installing Pip
##############
pip is Pythons package manager that allows users that allows third party packages to run. Unlocke utilizes a couple
third party packages.

Sometimes Linux distributions do not come preinstalled with pip. You will need to run the following command

Fedora/CentOS 8/CentOS Stream/RHEL
**********************************
Any Linux Distribution that utilizes RPM packages. Work with this method. This also includes Oracle Enterprise Linux and
OpenSUSE.
::
    sudo dnf install python3-pip

CentOS 7
********
.. note::   CentOS 7 does not come with Python3 by default. You will have to install it yourself. This guide does not cover that.
CentOS will require additional work to configure that is not covered by this guide. If you can it is advised to use CentOS Stream,
or move over to an LTS build of Ubuntu.
::
    sudo yum install python3-pip


Debian/Ubuntu
*************
This covers any Linux Distributions that uses apt. Primarily Debian based distributions. Examples not included in the
title are: Linux Mint, Deepin, Kali Linux.
::
    sudo apt install python3-pip

Installing packages via pip
###########################
.. note::   You need to be in the directory that has Unlocke's files.

You can install these packages via the following command
Test
::
    sudo pip3 install -r requirements.txt

