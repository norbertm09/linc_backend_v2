
from fastapi import APIRouter
router = APIRouter(prefix='/admin', tags=['admin'])

@router.get('/')
def index():
    return {{ "endpoint": "admin", "status": "ok" }}
