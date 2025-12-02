from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():



    response = "hody"


    
    
    return {"response": response}
