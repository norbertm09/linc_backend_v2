
from fastapi import APIRouter
router = APIRouter(prefix='/credits', tags=['credits'])

@router.get('/')
def index():
    return {{ "endpoint": "credits", "status": "ok" }}
