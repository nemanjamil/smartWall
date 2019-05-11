#! /bin/sh
BASEDIR=$(dirname "$0")
echo "$BASEDIR"
source $BASEDIR/../main_venv/bin/activate
python3 $BASEDIR/App.py