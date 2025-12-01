from fastapi import FastAPI
import os
from sandwichAPI import sandwich
app = FastAPI()


@app.get("/")
def read_root():

   

 
    value = sandwich()






    response = "howdy"


    
    
    return {"response": response, "sandwich_result": value}
