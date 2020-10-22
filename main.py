import flask
import psutil
from hurry.filesize import size
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RAM API</h1><p> Welcome to the RAM API</p>"

@app.route('/sys', methods=['GET'])
def system():
    return {
        "cpu_percent" : psutil.cpu_percent(),
        "virtual_memory" : {
            "available": size(psutil.virtual_memory().available), 
            "free": size(psutil.virtual_memory().free), 
            "percent": psutil.virtual_memory().percent, 
            "total": size(psutil.virtual_memory().total), 
            "used": size(psutil.virtual_memory().used)
        },
        "percentage_of_available_memory" : psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,
    }

app.run()