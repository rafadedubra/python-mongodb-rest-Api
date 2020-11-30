from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo #encontré esta libreria en un tutorial y me gustó para hacer la conexión con la bd
from bson import json_util
from bson.objectid import ObjectId
import json
import markdown.extensions.fenced_code
import os
import dotenv

dotenv.load_dotenv()

DBURL = os.getenv("URL")

app = Flask(__name__)

app.config['MONGO_URI'] = DBURL

mongo = PyMongo(app)


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string= markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json['user']
    if user:
        id = mongo.db.users.insert(
            {'user': user})
        response = jsonify({
            '_id': str(id),
            'user': user
        })
        response.status_code = 201
        return response
    else:
        return not_found()


@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mongo.db.users.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@app.route('/users/<_id>', methods=['PUT'])
def update_user(_id):
    user = request.json['user']
    if user:
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': user}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()

    
@app.route('/chat', methods=['POST'])
def create_chat():
    # Receiving Data
    user = request.json['user']
    chatname = request.json['chatname']
    message = request.json['message']

    if user and chatname and message:
        id = mongo.db.chat.insert(
            {'user': user, 'chatname': chatname, 'message': message})
        response = jsonify({
            '_id': str(id),
            'user': user,
            'chatname': chatname,
            'message': message
        })
        response.status_code = 201
        return response
    else:
        return not_found()    

@app.route('/chat', methods=['GET'])
def get_chats():
    chat = mongo.db.chat.find()
    response = json_util.dumps(chat)
    return Response(response, mimetype="application/json")

@app.route('/chat/<id>', methods=['GET'])
def get_chat(id):
    print(id)
    user = mongo.db.chat.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


@app.route('/chat/<id>', methods=['DELETE'])
def delete_chat(id):
    mongo.db.chat.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response

@app.route('/uschaters/<_id>', methods=['PUT'])
def update_chat(_id):
    user = request.json['user']
    chatname = request.json['chatname']
    message = request.json['message']
    if user and chatname and message and _id:
        mongo.db.chat.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'user': user, 'chatname': chatname, 'message': message}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)