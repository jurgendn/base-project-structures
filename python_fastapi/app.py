from fastapi import FastAPI
from src.routers import some_router

app = FastAPI()

# Include some routers here
app.include_router(some_router.router)


@app.get("/")
async def index():
    return "Hello World"