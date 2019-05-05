#! /bin/bash

export rpiPass="integra1234"
export rpiIP=192.168.0.24
export integraRoot="~/integra"
export saveLog="True"
rm ./src/static/log/*
if [ ${saveLog} = "True" ] 
    then
    sshpass -p ${rpiPass} scp -r pi@${rpiIP}:${integraRoot}/src/static/log/* ./src/static/log
fi
sshpass -p ${rpiPass} ssh pi@${rpiIP} "sudo pkill -f python3"
sshpass -p ${rpiPass} ssh pi@${rpiIP} "rm -rf ${integraRoot}/src"
sshpass -p ${rpiPass} ssh pi@${rpiIP} "mkdir ${integraRoot}/src"

sshpass -p ${rpiPass} scp -r ./src/* pi@${rpiIP}:${integraRoot}/src

echo "Got here"
export remoteRun="False"
if [ ${remoteRun} = "True" ] 
    then
    sshpass -p ${rpiPass} ssh pi@${rpiIP} "cd ${integraRoot} && \
    source ${integraRoot}/main_venv/bin/activate && \
    nohup python3 -m ptvsd --host 0.0.0.0 --port 5678 --wait ${integraRoot}/${1} &"
fi