# Simple flask app to serve the REST API

from flask import Flask, jsonify, request, abort

import iris

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return an json object
    return jsonify({'message':'Hello World'})

@app.route('/persistentclass', methods=['POST'])
def create_persistentclass():
    if not request.json or not 'test' in request.json:
        abort(400)
    obj=iris.cls('Demo.PersistentClass')._New()
    obj.Test=request.json['test']
    obj._Save()
    return jsonify({'id':obj._Id(),'test':obj.Test}), 201

@app.route('/persistentclass/<int:id>', methods=['GET'])
def get_one_persistentclass(id):
    if iris.cls('Demo.PersistentClass')._ExistsId(id):
        obj=iris.cls('Demo.PersistentClass')._OpenId(id)
        return jsonify({'id':id,'test':obj.Test})
    else:
        return jsonify({'error':'not found'}), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
