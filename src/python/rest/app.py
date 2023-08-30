# Simple flask app to serve the REST API

from flask import Flask, jsonify, request

import iris

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/persistentclass/<int:id>', methods=['GET'])
def get_one_persistentclass(id):
    if iris.cls('Demo.PersistentClass')._ExistsId(id):
        obj=iris.cls('Demo.PersistentClass')._OpenId(id)
        return jsonify({'id':id,'test':obj.Test})
    else:
        return jsonify({'error':'not found'}), 404
    
if __name__ == '__main__':
    app.run()
