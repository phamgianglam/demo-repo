from uuid import UUID, uuid4
from typing import List
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as sqlUUID
from sqlalchemy import MetaData
from sqlalchemy.orm import backref, declarative_base, lazyload, relationship

BaseModel = declarative_base(MetaData())


class Series(BaseModel):
    __tablename__ = "series"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    owner: str = Column(String, nullable=False, unique=False)
    date: int = Column(
        Integer,
        nullable=False,
    )


class Title(BaseModel):
    __tablename__ = "title"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    date: datetime = Column(DateTime, nullable=False)
    series_id: UUID = Column(
        sqlUUID(as_uuid=True), ForeignKey("series.id"), nullable=False, index=True
    )
    series: Series = relationship("Series", backref=backref("titles", lazy="subquery"))


class Dvd(BaseModel):
    __tablename__ = "dvd"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True)
    name: str = Column(String, ForeignKey("title.name"))
