from fastapi import FastAPI
from routers import users

app= FastAPI(title= "SaaS Lab API")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a SaaS Lab API"}
