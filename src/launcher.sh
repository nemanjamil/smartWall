#! /bin/sh
sudo ifconfig lo:2 192.168.201.1 netmask 255.255.255.255 up
BASEDIR=$(dirname "$0")
echo "$BASEDIR"
source $BASEDIR/../main_venv/bin/activate
python3 $BASEDIR/App.py