from flask import Flask , render_template , request , redirect , session
import base64

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    session['count']=0
    session['page_count']=0
    return redirect('/index')

@app.route('/index')
def index_index():
    if 'count' in session:
        session['page_count'] += 1
        session['count'] += 1
    else:
        session['page_count'] = 1
        session['count'] =1
        print("key 'key_name' does NOT exist")
    base64.urlsafe_b64decode('eyJjb3VudCI6MjcsInBhZ2VfY291bnQiOjl9===')
    return render_template('index.html')

@app.route('/index/twice')
def index_twice_index():
    if 'count' in session:
        session['page_count'] += 1
        session['count'] += 2
    else:
        session['page_count'] = 1
        session['count'] =2
        print("key 'key_name' does NOT exist")
    return render_template('index.html')

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    user_count=request.form['user_count']
    user_count = int(user_count)
    if 'count' in session:
        session['page_count'] += 1
        session['count'] += user_count
    else:
        session['page_count'] = 1
        session['count'] = user_count
        print("key 'key_name' does NOT exist")
    return render_template('index.html')

@app.route('/destroy_session')
def index_destroy():
    session.clear()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

