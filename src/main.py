from routes.user import router as userRouter
from config.settings import *

import uvicorn
from fastapi import FastAPI


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)


""" healtcheck for service"""
@app.get("/healthcheck", tags=["Root"])
async def read_root():
    return {"message": "Welcome to python app!"}

""" include routers"""
app.include_router(userRouter, tags=["User"])
