from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)

json_config = json.loads(open("config/config.json").read())


@app.route('/')
def index():

    if json_config['init']:
        return render_template('index.html')
    else:
        return render_template("config.html")


@app.route('/config/save', methods=['POST'])
def save_config():
    if request.method == 'POST':
        return 'Funciona'
    else:
        return abort(404)

#Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return 'No existe', 404