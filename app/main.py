from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="Rachmistrz Backend")

# rejestrujemy routery
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Hello from Rachmistrz Backend!"}

