from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

import app.models
from app.config import settings
from app.database import init_db
from app.routers import (client_router, role_router, ex_type_router, object_router, account_auth_router,
                                 employee_router)

app = FastAPI(
    title=settings.app_name,
    debug = settings.debug,
    docs_url = '/api/docs',
    redoc_url = '/api/redoc',
)
app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.cors_allowed_origins,
    allow_credentials= True,
    allow_methods= ['*'],
    allow_headers= ['*']
)

app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")

@app.get("/")
def root():
    return {"message": "оч советую перейти на /api/docs"}

app.include_router(client_router.router)
app.include_router(role_router.router)
app.include_router(ex_type_router.router)
app.include_router(object_router.router)
app.include_router(account_auth_router.router)
app.include_router(employee_router.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get('/health')
def health_check():
    return {"status": "ok"}