from fastapi import APIRouter

courses_api_router = APIRouter()

@courses_api_router.get("/courses/test")
async def get_test():
    return {"msg": "Hello World"}