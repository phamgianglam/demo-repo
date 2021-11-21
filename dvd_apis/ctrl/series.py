from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from ..schemas import SeriesPostModel
from ..model.models import Series



async def create_resource(series:SeriesPostModel, session:AsyncSession):
    new_series=Series(name=series.name, date=series.date)
    print(new_series.id_)
    session.add(new_series)
    await session.commit()
    return new_series