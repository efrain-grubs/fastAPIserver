from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
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
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"
                }
            ]
        }
    ]
)

    print(response.output_text)
    return {"message": response.output_text}
    

   

    
