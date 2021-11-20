from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from ..schemas import UserPostModel
from ..model.models import User


async def create_resource(user: UserPostModel, session: AsyncSession):
    data = User(**user.dict())
    print(data.citizen_id)
    session.add(data)
    await session.commit()
    return data


async def get_resource(session: AsyncSession, id: UUID = None):
    stmt = select(User)
    if id is not None:
        stmt = stmt.where(User.id_ == id)
        result = (await session.execute(stmt)).scalar_one()
    else:
        result = (await session.execute(stmt)).scalars().all()
    return result


async def delete_resource(session: AsyncSession, id=UUID):
    user = await get_resource(session, id)
    await session.delete(user)
    await session.commit()
