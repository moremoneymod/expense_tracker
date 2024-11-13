from fastapi import FastAPI
from backend_api.app.routes import transactions_routes
import uvicorn

app = FastAPI()

app.include_router(transactions_routes.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)