
from fastapi import APIRouter
router = APIRouter(prefix='/crypto', tags=['crypto'])

@router.get('/')
def index():
    return {{ "endpoint": "crypto", "status": "ok" }}
