
from fastapi import APIRouter
router = APIRouter(prefix='/notifications', tags=['notifications'])

@router.get('/')
def index():
    return {{ "endpoint": "notifications", "status": "ok" }}
