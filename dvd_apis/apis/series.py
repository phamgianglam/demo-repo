from fastapi import APIRouter, Depends, exceptions, HTTPException
from fastapi import Response
from typing import List

from ..model.depend import create_session
from ..schemas import SeriesModel, SeriesPostModel
from ..ctrl import series as ctrl
from sqlalchemy.exc import IntegrityError, NoResultFound

router = APIRouter()
PREFIX = "series"


@router.post("/", response_model=SeriesModel, status_code=201)
async def create_series(series: SeriesPostModel, session=Depends(create_session)):
    try:
        result = await ctrl.create_resource(series, session)
    except IntegrityError as exc:
        raise HTTPException(status_code=409, detail="duplicate")
    return result


@router.get("/{name}", response_model=SeriesModel, status_code=200)
async def get_series(name: str, session=Depends(create_session)):
    try:
        result = await ctrl.get_resource(name, session)
    except NoResultFound as exc:
        raise HTTPException(status_code=404, detail=f"{name} is not found")
    return result


@router.delete("/{name}")
async def delete_series(name, session=Depends(create_session)):
    try:
        await ctrl.delete_resource(name, session)
    except NoResultFound as exc:
        raise HTTPException(status_code=404, detail=f"{name} is not found")
    return Response(status_code=204)


@router.patch("/{name}")
async def patch_series(name, session=Depends(create_session)):
    try:
        await ctrl.patch_resource(name, session)
    except NoResultFound as exc:
        raise HTTPException(status_code=404, detail=f"{name} is not found")
    return Response(status_code=204)
