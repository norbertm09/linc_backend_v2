
from fastapi import APIRouter
router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/')
def index():
    return {{ "endpoint": "auth", "status": "ok" }}
