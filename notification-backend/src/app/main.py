import uvicorn
from fastapi import  FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.app.api import models, notifications, users
from src.app.database import engine

# uvicorn main:app --host 127.0.0.1 --port 8000 --env-file .env --reload
# uvicorn src.app.main:app --reload --host 127.0.0.1 --port 8000 --env-file .env


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Adding CORS middleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(notifications.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
