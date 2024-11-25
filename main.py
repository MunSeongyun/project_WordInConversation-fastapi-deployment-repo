from fastapi import FastAPI
from routers import vocabulary
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

origins = [
    'http://localhost:5173',
    'http://localhost:8080',
    'http://localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vocabulary.router)

@app.get('/')
async def main():
    return {
        'message':'hello'
    }