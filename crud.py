from sqlalchemy.orm import Session

import models, schemas

def get_cliente(db: Session, dni: int):
    return db.query(models.Cliente).filter(models.Cliente.CodiClie == dni).first()