from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        f = open("login.txt", "r")
        us = f.readline().strip()
        pw = f.readline().strip()
        f.close()
        
        if us == request.form["us"] and pw == request.form["pw"]:
            return "hello" + us
        else:
            return "User not recognized"
    
        
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        f = open("login.txt", "w")
        f.write(request.form["us"])
        f.write("\n")
        f.write(request.form["pw"])
        f.close()

        return "signup successful"
