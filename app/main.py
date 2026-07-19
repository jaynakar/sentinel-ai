from fastapi import FastAPI

from app.api.routes import router

from app.startup import initialize


app = FastAPI(
    title="Hybrid Fraud Detection API",
)


@app.on_event("startup")
def startup():

    initialize()


app.include_router(router)