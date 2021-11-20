from uuid import UUID
from pydantic import BaseModel, Field
from enum import Enum


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


class UserPostModel(BaseModel):
    name: str = Field(..., description="name")
    phone: str = Field(..., description="phone number")
    citizen_id: str = Field(..., description="citizen number", alias="citizenId")
    address: str = Field(..., description="address")
    district: DistrictEnum = Field(...)
    ward: WardEnum = Field(...)
    vip: bool = Field(False)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"


class UserModel(BaseModel):
    id_: UUID = Field(..., alias="id")
    name: str = Field(..., description="name")
    phone: str = Field(..., description="phone number")
    citizen_id: str = Field(..., description="citizen number", alias="citizenId")
    address: str = Field(..., description="address")
    district: DistrictEnum = Field(...)
    ward: WardEnum = Field(...)
    vip: bool = Field(False)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
