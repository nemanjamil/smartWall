import time
from flask import Flask, render_template, jsonify, request
from integraHWManager import IntegraHWManager
app = Flask(__name__)

mgr = IntegraHWManager(autoRefresh=True, 
autoRefreshPeriod=1.0, 
log=True,
logPeriod=20.0, 
logFilename="log.txt")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/measurements.json")
def measurements_json():
    return jsonify(mgr.getAllDicts())
# Used just for debug on the remote host. 
# Will be changed in production


app.run(host="0.0.0.0",port="5000")