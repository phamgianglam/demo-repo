from uuid import UUID, uuid4
from enum import Enum
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.types import Enum as PgEnum, String
from sqlalchemy import Column, Constraint
from sqlalchemy.dialects.postgresql import UUID as sqlUUID
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

BaseModel = declarative_base(MetaData())


class DistrictEnum(str, Enum):
    district_1 = "distrcit 1"
    district_2 = "distrcit 2"
    district_3 = "distrcit 3"
    district_4 = "distrcit 4"
    district_5 = "distrcit 5"
    district_6 = "distrcit 6"
    district_7 = "distrcit 7"


class WardEnum(str, Enum):
    ward_a = "ward 1"
    ward_b = "ward 2"
    ward_c = "ward 3"
    ward_d = "ward 4"
    ward_e = "ward 5"
    ward_f = "ward 6"
    ward_g = "ward 7"


class User(BaseModel):
    __tablename__ = "user"
    id_: UUID = Column("id", sqlUUID(as_uuid=True), default=uuid4(), primary_key=True)
    name: str = Column(String, nullable=False)
    phone: str = Column(String, nullable=False)
    citizen_id = Column(String, nullable=False, unique=True)
    address: str = Column(String, nullable=False)
    district: DistrictEnum = Column(PgEnum(DistrictEnum), nullable=False)
    ward: WardEnum = Column(PgEnum(WardEnum), nullable=False)
    vip: bool = Column(Boolean, default=False, nullable=False)

