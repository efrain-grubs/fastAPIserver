from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv
app = FastAPI()


@app.get("/")
def read_root():

   

    

    message = "hello world"


    
    
    return {"response": "no this is not a sandwich"}
