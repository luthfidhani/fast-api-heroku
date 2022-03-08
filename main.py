from fastapi import FastAPI
from fastapi.params import Form
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Success"}

@app.post("/")
async def index(query:str = Form(..., example='1+(1+2)*8')):
    return {"query": query, "result": eval(query)}