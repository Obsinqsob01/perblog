from flask import Flask, render_template
import json

app = Flask(__name__)

json_config = json.loads(open("config/config.json").read())


@app.route('/')
def index():

    if json_config['init']:
        return render_template('index.html')
    else:
        return render_template("config.html")
