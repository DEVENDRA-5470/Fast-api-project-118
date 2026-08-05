from fastapi import FastAPI , Depends ,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import requests
from database import SessionLocal,engine,Base
import models , schemas

Base.metadata.create_all(bind=engine)

app=FastAPI(description="This is My first FastAPI app")

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check(db:Session=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status":"ok","db":"connected ✅"}
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"DB connection failed : {str(e)} ❌")

@app.get("/")
def test():
    return {"Message":"Hello to FastAPI "}

@app.get("/product")
def get_product():
    resp=requests.get(f"https://dummyjson.com/products")
    data=resp.json()
    return data

