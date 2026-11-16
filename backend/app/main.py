from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Iniciativas Sustentáveis", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_methods=["*"], allow_headers=["*"])


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/iniciativas", response_model=list[schemas.IniciativaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(models.Iniciativa).order_by(models.Iniciativa.id.desc()).all()


@app.post("/api/iniciativas", response_model=schemas.IniciativaOut, status_code=201)
def criar(dados: schemas.IniciativaCreate, db: Session = Depends(get_db)):
    item = models.Iniciativa(**dados.model_dump())
    db.add(item); db.commit(); db.refresh(item)
    return item


@app.put("/api/iniciativas/{item_id}", response_model=schemas.IniciativaOut)
def atualizar(item_id: int, dados: schemas.IniciativaUpdate, db: Session = Depends(get_db)):
    item = db.get(models.Iniciativa, item_id)
    if not item: raise HTTPException(404, "Iniciativa não encontrada")
    for campo, valor in dados.model_dump().items(): setattr(item, campo, valor)
    db.commit(); db.refresh(item)
    return item


@app.delete("/api/iniciativas/{item_id}", status_code=204)
def excluir(item_id: int, db: Session = Depends(get_db)):
    item = db.get(models.Iniciativa, item_id)
    if not item: raise HTTPException(404, "Iniciativa não encontrada")
    db.delete(item); db.commit()


@app.get("/api/indicadores", response_model=schemas.Indicadores)
def indicadores(db: Session = Depends(get_db)):
    total = db.query(func.count(models.Iniciativa.id)).scalar() or 0
    finalizadas = db.query(func.count(models.Iniciativa.id)).filter(models.Iniciativa.progresso == 100).scalar() or 0
    media = db.query(func.avg(models.Iniciativa.progresso)).scalar() or 0
    return {"iniciativas": total, "finalizadas": finalizadas, "progresso_medio": round(float(media), 1)}
