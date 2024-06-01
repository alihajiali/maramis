from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

templates = Jinja2Templates(directory="templates/")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def read_root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=8000, reload=True, workers=3)