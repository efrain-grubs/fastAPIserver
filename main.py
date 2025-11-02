from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    
    
    return {"hello world. pleaseeeee work is the pipeline working "}
