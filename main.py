from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your Replit and local browser to call the API
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://*.replit.app",
    "https://*.repl.co",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}! Welcome to the API."}

