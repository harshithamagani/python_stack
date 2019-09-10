from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def display_dojo():
    return 'Dojo'

@app.route('/success')
def success():
    return "success"

@app.route('/say/<name>')
def hello_flask(name):
    print(name)
    return f"Hello {name}!"

@app.route('/repeat/<num>/<value>')
def displayRepeatValue(num,value):
    return int(num)*value

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."


if __name__== "__main__":
    app.run(debug=True)
