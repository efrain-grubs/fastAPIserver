from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():



    response = "We've just made changes"
    "lets watch  cicd in action "


    
    
    return {"response": response}
