from flask import Flask , jsonify , request

tasks = [
    {"id": 1, "title": "Learn Flask", "completed": True},
    {"id": 2, "title": "Build API", "completed": False},
    {"id": 3, "title": "Upload to GitHub", "completed": False}
]


app = Flask(__name__)

@app.route('/api/tasks/', methods=['GET'] , strict_slashes = False)
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks/', methods=['POST'], strict_slashes=False)
def create_task():
    data = request.get_json()
    
    # Create new task with next ID
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get('title'),
        "completed": False
    }
    
    # ACTUALLY SAVE IT to the list
    tasks.append(new_task)
    
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:id>' , methods = ['PUT'])
def update_task(id):
    data = request.get_json()
    
    for task in tasks:
        if task['id'] == id:
            task['completed'] = data.get('completed')
            return jsonify({"message": f"Task status updated successfully to {task['completed']}"}), 200
    return jsonify({"error": "Task not found"}), 404


@app.route('/api/tasks/<int:id>' , methods = ['DELETE'])
def delete_task_by_id(id):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"}), 200
        
    return jsonify({"error": "Task not found"}), 404









@app.route('/')
def home():
    return 'Hello Flask!'

@app.route('/about')
def about():
    return "This is a about page"


@app.route('/contact')
def contact():
    return "this is our email: Jandaghi14@gmail.com"

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

@app.route('/greet/<name>/<age>')
def greet(name , age):
    return f"{name} is {age} years ald!"

@app.route('/calculate/<int:num>')
def calculate(num):
    return f"Double of {num} is {num * 2}"

@app.route('/api/user/<user_name>')
def api_user(user_name):
    user_data = {
        'name' : user_name,
        'status' : 'active',
        'posts' : 42 
        
    }
    return jsonify(user_data)


    



if __name__ == '__main__':
    app.run(debug=True)