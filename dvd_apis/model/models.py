from uuid import UUID, uuid4
from typing import List
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, String
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as sqlUUID
from sqlalchemy import MetaData
from sqlalchemy.orm import backref, declarative_base, relationship

BaseModel = declarative_base(MetaData())


class Series(BaseModel):
    __tablename__ = "series"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    date: datetime = Column(DateTime, nullable=False,)
    titles: List[str] = relationship("Title", backref=backref("series"))


class Title(BaseModel):
    __tablename__ = "title"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    date: datetime = Column(DateTime, nullable=False)
    series_name: str = Column(String, ForeignKey("series.name"))


class Dvd(BaseModel):
    __tablename__ = "dvd"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True)
    name: str = Column(String, ForeignKey("title.name"))
