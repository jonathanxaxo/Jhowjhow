from pydantic import BaseModel, ConfigDict, Field


class IniciativaBase(BaseModel):
    nome: str = Field(min_length=3, max_length=120)
    unidade: str = Field(min_length=2, max_length=100)
    impacto_estimado: str = Field(min_length=3, max_length=220)
    progresso: float = Field(ge=0, le=100)


class IniciativaCreate(IniciativaBase):
    pass


class IniciativaUpdate(IniciativaBase):
    pass


class IniciativaOut(IniciativaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Indicadores(BaseModel):
    iniciativas: int
    finalizadas: int
    progresso_medio: float
