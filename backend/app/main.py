from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import ToDo
from app.database import engine
from app.routes.todo import router as todo_router
app = FastAPI(title="Todo API")

# Create DB tables
ToDo.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router)
@app.get("/")
def root():
    return {"message": "FastAPI is running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "OK"}