from flask import Flask # Import Flask module

app = Flask(__name__) #Create an object named `app` from imported Flask module

@app.route("/")
def hello():              #Create a function `hello` which returns a string `Hello World`
    return "Hello World"

@app.route("/bye")
def goodbye():       #create a function 'Goodbye which returns string "Goodbye" 
    return "Goodbye"

@app.route("/third/subthird")
def third():
    return "This is a double path"

@app.route("/fourth/<string:id>")
def fourth(id):
    output = f"Your ID is {id}"
    return output

if __name__ == '__main__':

    app.run(debug=True, port=5000)
    # app.run(host= '0.0.0.0', port=8081)