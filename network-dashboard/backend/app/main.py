from fastapi import FastAPI

app = FastAPI(title="Network Dashboard API")


@app.get("/")
def read_root():
    return {"message": "Network Dashboard API is running"}
