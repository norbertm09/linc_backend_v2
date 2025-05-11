
from fastapi import APIRouter
router = APIRouter(prefix='/insurance', tags=['insurance'])

@router.get('/')
def index():
    return {{ "endpoint": "insurance", "status": "ok" }}
