from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def get_user_info(user_id: str):
    return {"user_id": user_id, "rating": 1000, "attempts_left": 3}
