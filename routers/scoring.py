
from fastapi import APIRouter
router = APIRouter(prefix='/scoring', tags=['scoring'])

@router.get('/')
def index():
    return {{ "endpoint": "scoring", "status": "ok" }}
