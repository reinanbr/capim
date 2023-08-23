
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI(debug=True,docs_url="/help")
origins = ["*"]

app.mount("/static", StaticFiles(directory="src/static"), name="static")


templates = Jinja2Templates(directory="src/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get('/', response_class=HTMLResponse)
async def start(request:Request):
    client = request.headers
    print(client)
    return templates.TemplateResponse('index.html',{"request": request,"client":client})

