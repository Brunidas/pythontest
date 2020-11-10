from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Cliente(Base):
	__tablename__ = "clientes"

	CodiClie = Column(Integer) # es el DNI de la persona
	NumeCta = Column(Integer)
	FaxClie = Column(String)

