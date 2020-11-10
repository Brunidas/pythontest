from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/cliente/{dni}", response_model=schemas.Cliente)
def read_Cliente(dni: int, db: Session = Depends(get_db)):
    db_Cliente = crud.get_cliente(db, dni=dni)
    if db_Cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_Cliente