from fastapi import FastAPI

app = FastAPI(title="Todo API")

@app.get("/")
def root():
    return {"message": "FastAPI is running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "OK"}