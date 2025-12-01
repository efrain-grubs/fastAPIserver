from fastapi import FastAPI
from openai import OpenAI
import os
app = FastAPI()
client = OpenAI(os.getenv("API_KEY"))

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
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"
                    }
                ]
            }
        ]
    )

    print(response.output_text)
    
    
    return {"response": response.output_text}
