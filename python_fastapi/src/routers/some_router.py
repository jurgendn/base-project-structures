from fastapi import APIRouter

router = APIRouter(prefix="/some-router")


@router.get("/some-endpoint")
async def some_feature():
    return {"Some": "Features"}