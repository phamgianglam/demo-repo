from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.orm.session import Session
from ..schemas import SeriesPostModel
from ..model.models import Series


async def create_resource(series: SeriesPostModel, session: AsyncSession):
    new_series = Series(name=series.name, date=series.date)
    session.add(new_series)
    await session.commit()
    return new_series


async def get_resource(name: str, session: AsyncSession):
    stm = select(Series).where(Series.name == name)
    result = (await session.execute(stm)).scalar_one()
    print(Series.titles)
    return result
