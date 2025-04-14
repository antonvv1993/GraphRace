from fastapi import APIRouter
from app.models.game_state import GameSession

router = APIRouter()
sessions = {}

@router.get("/start")
def start_game(user_id: str):
    session = GameSession()
    sessions[user_id] = session
    return {"candles": session.get_game_data()}

@router.post("/submit")
def submit_prediction(user_id: str, prediction: str):
    session = sessions.get(user_id)
    if not session:
        return {"error": "no active session"}
    correct = session.get_target_direction()
    return {"result": prediction == correct, "correct_direction": correct}
