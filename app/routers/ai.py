from fastapi import APIRouter
from app.schemas.ai_schema import AIRequest
from app.services.ai_service import generate_response

router = APIRouter()

@router.post("/ask")
def ask(req: AIRequest):
    message = generate_response(req.text)
    return {"mensagem": message}
