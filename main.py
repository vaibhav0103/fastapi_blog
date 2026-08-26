from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home Page"})

@app.get("/api/posts")
def get_posts():
    return  posts