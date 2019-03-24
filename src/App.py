import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Used just for debug on the remote host. 
# Will be changed in production
app.run(host="0.0.0.0",port="5000")