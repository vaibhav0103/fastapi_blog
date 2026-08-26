from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts : list[dict] = [{
    "title": "title of post 1",
    "content": "content of post 1",
    "id": 1
},
{
    "title": "title of post 2",
    "content": "content of post 2",
    "id": 2
}]

@app.get("/")
@app.get("/home")
async def home():
    return {"message": "Hello World"}

@app.get("/home-html", response_class=HTMLResponse, include_in_schema=False)
async def home_html():
    return f"<h1>{posts[0]['title']}</h1><p>{posts[0]['content']}</p>"

@app.get("/posts")
async def get_posts():
    return  posts