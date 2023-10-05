from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="public", html=True))


