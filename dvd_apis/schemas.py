from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class SeriesPostModel(BaseModel):
    name: str = Field(..., description="name")
    date: datetime = Field(..., description="year of first title", alias="year")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {"example": {"name": "abc", "year": "2021-11-21T17:56:04.305745"}}


class SeriesModel(BaseModel):
    id_: UUID = Field(..., alias="id")
    name: str = Field(..., description="name")
    date: datetime = Field(..., description="date")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"


class SeriesPatchModel(BaseModel):
    name: str = Field(None, description="name")
    date: datetime = Field(None, description="date")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
