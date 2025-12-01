from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()
# API_KEY = os.getenv("API_KEY")
# print("something",API_KEY)
client = OpenAI(api_key="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")

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

    # response = "h  "
    
    
    return {"response": message}
