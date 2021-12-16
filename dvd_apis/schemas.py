from datetime import datetime
from typing import List, Any, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, validator

MAX_YEAR = 2030
MIN_YEAR = 1895


def check_year(cls, year: int) -> None:
    # for now year should between 1895 and 2030
    if not year in range(MIN_YEAR, MAX_YEAR):
        raise ValueError(f"year should be in range {MIN_YEAR}, {MAX_YEAR}")
    else:
        return year


class SeriesPostModel(BaseModel):
    name: str = Field(..., description="name")
    owner: str = Field(..., description="owner")
    date: Optional[int] = Field(..., description="year of first title", alias="year")
    _check_date_ = validator("date", pre=True, allow_reuse=True)(check_year)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {"example": {"name": "haryr porter", "owner": "Wanner Bros", "year": 2001}}


class SeriesModel(BaseModel):
    id_: UUID = Field(..., alias="id")
    name: str = Field(..., description="name")
    owner: str = Field(..., description="owner")
    date: int = Field(..., description="date")
    titles: List[Any] = Field(..., description="all titles of series")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {
            "example": {"id": uuid4(), "name": "haryr porter", "year": 2001, "owner": "Wanner Bros"}
        }


class SeriesPatchModel(BaseModel):
    name: str = Field(None, description="name")
    owner: str = Field(..., description="owner")
    date: int = Field(None, description="date")
    _check_date_ = validator("date", pre=True, allow_reuse=True)(check_year)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {"example": {"name": "haryr porter", "year": 2001, "owner": "Wanner Bros"}}


class TitlesPostModel(BaseModel):
    name: str = Field(..., description="name")
    owner: str = Field(..., description="owner")
    date: int = Field(..., description="year of first title", alias="year")
    series_id: UUID = Field(..., description="id of series")
    _check_date_ = validator("date", pre=True, allow_reuse=True)(check_year)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {
            "example": {
                "name": "harry potter and the philosopher's stone",
                "year": 2001,
                "owner": "Wanner Bros",
            }
        }


class TitleModel(BaseModel):
    id_: UUID = Field(..., alias="id")
    name: str = Field(..., description="name")
    owner: str = Field(..., description="owner")
    date: int = Field(..., description="date")
    series_id: UUID = Field(..., description="id of series")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {
            "example": {"id": uuid4(), "name": "haryr porter", "year": 2001, "owner": "Wanner Bros"}
        }
