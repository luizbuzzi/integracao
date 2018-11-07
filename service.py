#!flask/bin/python
from flask import Flask, abort, request
import requests
import json

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def time():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    variable = request.args.get('variable')
    payload = {'origins':origin,
               'destinations':destination,
               'key':'AIzaSyBb8sJ270Ka_6a3vH1g4CAEpeUxMVDVIhY'}
    r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json',
                    params=payload)
    
    data = json.loads(r.text)['rows'][0]['elements'][0]['duration']['value']
    
    return str(data)


if __name__ == '__main__':
    app.run(debug=True)
