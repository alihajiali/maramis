from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="templates/")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def read_root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})



if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=10003, reload=True, workers=3)