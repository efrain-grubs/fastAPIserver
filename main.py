from fastapi import FastAPI
import os
from sandwichAPI import sandwich
app = FastAPI()


@app.get("/")
def read_root():

   

 

    response = "hello world"


    
    
    return {"response": response}
