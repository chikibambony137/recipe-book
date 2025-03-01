from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/")
async def main():
    return {"Hello": "World!"}

app.include_router(router)