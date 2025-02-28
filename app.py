# Import the necessary libraries 
from flask import Flask,jsonify,request


app = Flask(__name__)

# Create a sample data
users = [
    {'id':1,'name':'Aman','email':'aman@gmail.com'},
    {'id':2,'name':'Bhavesh','email':'bhavesh@gmail.com'}
]

# Route to print all the users
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)

# Route to print specified Users
@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id),None)
    return jsonify(user) if user else ('User not found',404)

#Route to add new Users
@app.route('/users',methods=['POST'])
def add_users():
    data = request.json
    new_user = {
        'id':len(users)+1,
        'name':data['name'],
        'email':data['email']
    }
    users.append(new_user)
    return jsonify(new_user),201

#Route to update specific User
@app.route('/users/<int:user_id>',methods=['PUT'])
def update_users(user_id):
    user = next((u for u in users if u['id'] ==user_id),None)
    if user:
        data =request.json
        user.update(data)
        return jsonify(user)
    return ('User not found',404)

#Route to delete User
@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_users(user_id):
    global users
    users = [u for u in users if u['id']!= user_id]
    return ('User deleted',204)

#Run the Project
if __name__ == '__main__':
    app.run(debug=True)
