# 4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def forms():
    return render_template("forms.html")

@app.route("/results",methods=["POST"])
def show():
    name=request.form["name"]
    age=request.form["age"]
    city=request.form["city"]
    return render_template("results.html",name=name, age=age, city=city)

if __name__=="__main__":
    app.run(debug=True)