from fastapi import APIRouter, Depends, exceptions, HTTPException
from typing import List
from ..model.depend import create_session
from ..schemas import UserModel, UserPostModel
from ..ctrl.user import create_resource, get_resource, delete_resource
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter()
PREFIX = "user"


@router.post("/", response_model=UserModel, status_code=201)
async def create_user(user: UserPostModel, session=Depends(create_session)):
    try:
        result = await create_resource(user, session)
    except IntegrityError as exc:
        raise HTTPException(status_code=409, detail="duplicate")
    return result


@router.get("/", status_code=200, response_model=List[UserModel])
async def list_users(session=Depends(create_session)):
    result = await get_resource(session=session)
    return result


@router.get("/{id}", status_code=200, response_model=UserModel)
async def get_user(id, session=Depends(create_session)):
    try:
        result = await get_resource(session, id)
    except NoResultFound as exc:
        raise HTTPException(status_code=404, detail="not found")
    return result


@router.delete("/{id}", status_code=204)
async def delete_user(id, session=Depends(create_session)):
    try:
        await delete_resource(session, id)
    except NoResultFound as exc:
        raise HTTPException(status_code=404, detail="not found")
