from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db  # Се увезува функцијата за иницијализација на базата
from app.routers import qr, urls


# Се дефинира lifespan менаџер за настани при вклучување и исклучување
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup чекор: Креирај ги сите табели во базата автоматски
    await init_db()
    yield
    # Shutdown чекор: Тука може да се чистат ресурси по потреба


# Се регистрира lifespan во FastAPI апликацијата
app = FastAPI(lifespan=lifespan)

origins = ["http://localhost:3000", "https://shortlink.lol"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(urls.router)
app.include_router(qr.router)