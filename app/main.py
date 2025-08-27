from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class Script(BaseModel):
    name: str
    description: str
    code: str


@app.post("/scripts")
def create_script(script: Script):
    return {"message": "Script created successfully"}






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
