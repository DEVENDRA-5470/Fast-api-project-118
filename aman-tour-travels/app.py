from flask import Flask,render_template
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
    return "Connected To backend ✅"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup")
def register():
    return render_template("register.html")

if __name__=="__main__":
    app.run(port=5000,debug=True)