from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.post("/hello")

#def hello(name = Body(embed=True)):
def hello(data = Body()):
    name = data["name"]
    age = data["age"]
    return {"message": f"{name}, ваш возраст - {age}"}

def hello1(date = Body()):
    name = date["name"]
    age = date["age"]
    return{"message": f"{name}, ваш возраст - {age}"}
