from fastapi import FastAPI
import os
from dotenv import load_dotenv
from sandwichAPI import sandwich
app = FastAPI()


@app.get("/")
def read_root():

   

    response = sandwich()

    # message = "hello world"


    
    
    return {"response": response}
