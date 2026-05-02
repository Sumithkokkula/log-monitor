from fastapi import FastAPI, Depends, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_home():
    return FileResponse("static/index.html")

# Create DB tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/logs")
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    db_log = models.Log(level=log.level, message=log.message)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


@app.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return db.query(models.Log).all()


@app.get("/logs/filter")
def filter_logs(level: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Log)
    if level:
        query = query.filter(models.Log.level == level)
    return query.all()
@app.get("/logs/search")
def search_logs(keyword: str, db: Session = Depends(get_db)):
    return db.query(models.Log).filter(
        models.Log.message.contains(keyword)
    ).all()



