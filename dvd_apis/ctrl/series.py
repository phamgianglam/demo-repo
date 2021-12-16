from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.sql.expression import update
from ..schemas import SeriesPostModel, SeriesPatchModel
from ..model.models import Series


async def create_resource(series: SeriesPostModel, session: AsyncSession):
    print(series.date)
    new_series = Series(name=series.name, owner=series.owner, date=series.date)
    session.add(new_series)
    await session.commit()
    await session.refresh(new_series)
    return new_series


async def get_resource(name: str, session: AsyncSession):
    stm = select(Series).where(Series.name == name)
    result = (await session.execute(stm)).scalars().one()
    return result


async def delete_resource(name: str, session: AsyncSession):
    stm = select(Series).where(Series.name == name)
    series = (await session.execute(stm)).scalars().one()
    await session.delete(series)
    await session.commit()
    return


async def patch_resource(name: str, patch_data: SeriesPatchModel, session: AsyncSession):
    stm = select(Series).where(Series.name == name)
    update(Series).where(Series.name == name).values(**patch_data.dict())
    await session.commit()
