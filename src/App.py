import time
from flask import Flask, render_template, jsonify, request, send_from_directory
from integraHWManager import IntegraHWManager
from os import path
import glob
import datetime
import re
app = Flask(__name__)


thisDir = path.dirname(__file__) + "/"
logfileExpression = thisDir + "static/log/logfile{0}.csv"
idxOfCurrentLogfile = len(glob.glob(logfileExpression.format('*')))

mgr = IntegraHWManager(autoRefresh=True, 
                       autoRefreshPeriod=0.5, 
                       log=True,
                       logPeriod=20.0, 
                       logFilename=logfileExpression.format(idxOfCurrentLogfile))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/measurements.json")
def measurements_json():
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

# Used just for debug on the remote host. 
# Will be changed in production


app.run(host="0.0.0.0",port="5000")