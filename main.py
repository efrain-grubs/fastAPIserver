from fastapi import FastAPI
import os
from sandwichAPI import sandwich
app = FastAPI()


@app.get("/")
def read_root():

   

 
    sandwich = sandwich()
    response = "hello world"


    
    
    return {"response": response, "sandwich_result": sandwich}
