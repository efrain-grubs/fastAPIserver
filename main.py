from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():



    response = "how dy"


    
    
    return {"response": response}
