from fastapi import FastAPI
from uvicorn import run
from database import Base, engine
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['127.0.0.1:3000', 'localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    run('main:app', reload=True)