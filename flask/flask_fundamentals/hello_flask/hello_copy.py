from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',parse='hello',times=10)

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."


if __name__== "__main__":
    app.run(debug=True)
