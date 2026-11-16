from sqlalchemy import Column, Float, Integer, String
from .database import Base


class Iniciativa(Base):
    __tablename__ = "iniciativas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    unidade = Column(String(100), nullable=False)
    impacto_estimado = Column(String(220), nullable=False)
    progresso = Column(Float, nullable=False, default=0)
