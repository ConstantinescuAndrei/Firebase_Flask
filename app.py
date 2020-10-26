from flask import Flask, request
import pyrebase

config = {
    "apiKey": "AIzaSyDY2ynYDDC5LMRhqZaM9x5xjDwryDAwJII",
    "authDomain": "monitoringanimalparametersapi.firebaseapp.com",
    "databaseURL": "https://monitoringanimalparametersapi.firebaseio.com",
    "projectId": "monitoringanimalparametersapi",
    "storageBucket": "monitoringanimalparametersapi.appspot.com",
    "messagingSenderId": "1042253543113",
    "appId": "1:1042253543113:web:79dd8f9a6f5013aef87f18",
    "measurementId": "G-VQRT3VD9BY"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#db.child("names").push({"name":"Andrei"})
#db.child("names").update({"name":"Codrut"})
#users = db.child("names").child("name").get()
#print(users.val())
db.child("names").remove()

data = {"name": "CS GO",
        "site": "faceit.com",
        "rank": 4
}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello World!"

@app.route('/temperature/<string:temperature>', methods=['POST'])
def game():
    temperature = request.args.get("temperature")
    db.child("temperature_sensor_data").push(temperature)
    return "<h1>Data was added with succes !!! </h1>"

if __name__ == '__main__':
    app.run()
