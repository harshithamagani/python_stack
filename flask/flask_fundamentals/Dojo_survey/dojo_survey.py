from flask import Flask, render_template,request,redirect

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info", methods=['POST'])
def info_form():
    print(request.form)
    name_from_form = request.form["name"]
    location_from_form =  request.form["location"]
    lang_from_form =  request.form["lang"]
    comment_from_form =  request.form["comment"]
    gender_from_form = request.form["gender"]
    termsNCon_from_form =  request.form["termsNCon"]
    return render_template("show.html", name_from_form=name_from_form , location_from_form=location_from_form, lang_from_form=lang_from_form, comment_from_form=comment_from_form, gender_from_form=gender_from_form,termsNCon_from_form=termsNCon_from_form)

if __name__=="__main__":
    app.run(debug=True)
