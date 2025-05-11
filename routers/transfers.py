
from fastapi import APIRouter
router = APIRouter(prefix='/transfers', tags=['transfers'])

@router.get('/')
def index():
    return {{ "endpoint": "transfers", "status": "ok" }}
