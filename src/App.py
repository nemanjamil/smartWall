hostedLocally = False
import time
from flask import Flask, render_template, jsonify, request, send_from_directory
if(not hostedLocally):
    from integraHWManager import IntegraHWManager
from os import path, remove
import glob
import datetime
import re
import threading
import subprocess
import logging
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/measurements.json")
def measurements_json():
    if(hostedLocally):
        return send_from_directory("../demo/wall_test_files", 
                            "measurements.json")
    return jsonify(mgr.getAllDicts())

def sortKeyFunction(element):
    p = re.compile(logfileExpression.format("(.*)"))
    val = p.findall(element)[0]
    return int(val)

@app.route("/logs")
def getLogs():
    return render_template("logs.html", 
        files=sorted(glob.glob(logfileExpression.format("*")), key=sortKeyFunction), 
        pathModule=path)

@app.route("/logfile/<path:filename>")
def getLogfile(filename):
    return send_from_directory("static/log", 
                                filename)

@app.route("/clearAll")
def clearLogFiles():
    filenames = glob.glob(logfileExpression.format("*"))
    for filename in filenames:
        remove(filename)
    mgr.reInitLogfile(logfileExpression.format(0))
    return "Cleared {0} logfiles".format(len(filenames))
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
# Used just for debug on the remote host. 
# Will be changed in production

if(not hostedLocally):
    thisDir = path.dirname(__file__) + "/"
    logfileExpression = thisDir + "static/log/logfile{0}.csv"
    idxOfCurrentLogfile = len(glob.glob(logfileExpression.format('*')))

    mgr = IntegraHWManager(autoRefresh=True, 
                        autoRefreshPeriod=0.5, 
                        log=True,
                        logPeriod=20.0, 
                        logFilename=logfileExpression.format(idxOfCurrentLogfile))

    def runChrome():
        print("Starting chrome")
        subprocess.run(["bash", thisDir + "launch_chromium.sh"])

    chromeThread = threading.Thread(target=runChrome)
    chromeThread.daemon = True
    chromeThread.start()
log = logging.getLogger("werkzeug")
log.setLevel(logging.WARNING)
app.run(host="0.0.0.0",port="5000",debug=False)