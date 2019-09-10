from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def display8By8Board():
    return render_template('index.html', num1=8 , num2=8, color1='lightskyblue',color2='lightpink')

@app.route('/<num1>')
def display8ByNumBoard(num1):
    num1=int(num1)
    return render_template('index.html',num1=num1,num2=8,color1='lightskyblue',color2='lightpink')

@app.route('/<num1>/<num2>')
def displayNum1ByNum2Board(num1,num2):
    num1=int(num1)
    num2=int(num2)
    return render_template('index.html',num1=num1,num2=num2,color1='lightskyblue',color2='lightpink')

@app.route('/<num1>/<num2>/<color1>/<color2>')
def displayNum1ByNum2BoardColor(num1,num2,color1,color2):
    num1=int(num1)
    num2=int(num2)
    return render_template('index.html',num1=num1,num2=num2,color1=color1,color2=color2)

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__== "__main__":
    app.run(debug=True)
