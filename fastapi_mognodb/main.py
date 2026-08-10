from fastapi import FastAPI
from database.connection import connect_database
from routes.auth import router as auth_router
connect_database()

app=FastAPI(
    title="Tour & Travel Serivices API",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/health")
async def health_check():
    return {"status":"ok" , "mongodb":"Connected ✅"}
    