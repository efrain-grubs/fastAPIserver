from fastapi import FastAPI
import os
from dotenv import load_dotenv
app = FastAPI()


@app.get("/")
def read_root():

   

    

    message = "hello world"


    
    
    return {"response": "no this is not a sandwich"}
