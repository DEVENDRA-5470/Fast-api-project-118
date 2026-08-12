from flask import Flask,render_template,request,redirect,url_for
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

app.secret_key=os.getenv("SECRET_KEY","this-is-secure-token-123456")

FASTAPI_URL=os.getenv("FASTAPI_URL")

@app.route("/health")
def backend_health():
    resp=requests.get(FASTAPI_URL+"health")
    return {"message":"Connected To backend ✅","Response":resp.json()}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup",methods=["GET","POST"])
def register():
    if request.method=="POST":
        data={
            "full_name":request.form.get("full_name"),
            "email":request.form.get("email"),
            "phone":request.form.get("phone"),
            "password":request.form.get("password")
        }
        
        response=requests.post(f"{FASTAPI_URL}auth/register",json=data)
        
        if response.status_code==200:
            return redirect(url_for("login"))
        
        
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(port=5000,debug=True)