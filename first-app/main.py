from fastapi import FastAPI , Depends ,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import requests
from database import SessionLocal,engine,Base
import models , schemas
import json

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

@app.post("/create_staff")
def create(staff:schemas.StaffCreate , db:Session = Depends(get_db)):
    new_staff=models.Staff(emp_name=staff.emp_name,emp_age=staff.emp_age,emp_city=staff.emp_city)
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff


@app.get("/staff")
def get_all_staff(db:Session = Depends(get_db)):
    staff=db.query(models.Staff).all() # select * from staff
    return staff

@app.get("/staff/{staff_id}")
def get_all_staff(staff_id:int ,db:Session = Depends(get_db)):
    staff=db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    return staff

@app.post("/staff/bulk-upload")
def bulk_upload_staff(db:Session=Depends(get_db)):
    try:
        with open("staff_data.json","r") as f:
            staff_list=json.load(f)
    except Exception as e:
        raise HTTPException(status_code=400 , detail=f" Error {str(e)}")

    created=[]
    for item in staff_list:
        new_staff=models.Staff(
            emp_name=item["emp_name"],
            emp_age=item["emp_age"],
            emp_city=item["emp_city"],
        )
        db.add(new_staff)
        created.append(new_staff)
    db.commit()
    for staff in created:
        db.refresh(staff)
    return {"Inserted ":len(created),"staff":created}

@app.delete("/staff/{staff_id}")
def delete_staff(staff_id:int ,db: Session = Depends(get_db)):
    staff=db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    if not staff:
        raise HTTPException(status_code=404)
    db.delete(staff)
    db.commit()
    return {"Message":f"Staff with id :{staff_id} has been Deleted ✅ "}

@app.delete("/staff")
def delete_all_staff(confirm: bool=False,db: Session = Depends(get_db)):
    if not confirm:
        raise HTTPException(status_code=400, detail="This will delete All Staff records. Pass ?confirm=true to proceed")
    staff=db.query(models.Staff).delete()
    db.commit()
    return {"Message":f"Deleted {staff} ✅ "}

# Update and partrial update
@app.put("/staff/{staff_id}")
def full_update_staff(staff_id : int ,staff: schemas.StaffCreate , db:Session= Depends(get_db)):
    existing_staff=db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    if not existing_staff:
        raise HTTPException(status_code=404 ,detail=f"Staff with id {staff_id} not found")

    existing_staff.emp_name=staff.emp_name
    existing_staff.emp_age=staff.emp_age
    existing_staff.emp_city=staff.emp_city

    db.commit()
    db.refresh(existing_staff)
    return existing_staff





