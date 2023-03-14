from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {"message":"Hello World"}

@app.get('/blog/all')
def get_all_blog():
    return "All blogs"

@app.get('/blog/{id}')
def get_blog(id:int):
    return {"message":f"Blog with an ID {id}"}

