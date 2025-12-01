from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()
# API_KEY = os.getenv("API_KEY")
# print("something",API_KEY)
client = OpenAI(api_key="hi")

@app.get("/")
def read_root():

    response = client.responses.create(
        model="gpt-5",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "What teams are playing in this image?",
                    },
                    {
                        "type": "input_image",
                        "image_url": "https://images.unsplash.com/photo-1517649763962-0c623066013b"

                    }
                ]
            }
        ]
    )

    

    message = response.output_text

    # response = "h "
    
    
    return {"response": "no this is not a sandwich"}
