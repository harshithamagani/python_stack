from flask import Flask, render_template

app=Flask(__name__)
@app.route('/play')
def hello_world():
    return render_template('index.html')

@app.route('/play/<num>')
def hello_play(num):
    times = int(num)
    return render_template('index.html', times=times)

@app.route('/play/<num>/<color>')
def hello_play_color(num,color):
    times = int(num)
    return render_template('index.html', times=times,color=color)

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__== "__main__":
    app.run(debug=True)
