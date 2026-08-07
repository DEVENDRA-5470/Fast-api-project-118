from fastapi import FastAPI,HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI=os.getenv("MONGODB_URI")

app=FastAPI()
client=AsyncIOMotorClient(MONGO_URI)

@app.get("/health")
async def health_check():
    try:
        await client.admin.command("ping")
        return {"status":"ok" , "mongodb":"Connected ✅"}
    except Exception as e:
        raise HTTPException(status_code=503 ,detail=f"MongoDB Connectionn failed {str(e)}")