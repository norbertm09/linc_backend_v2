
from fastapi import APIRouter
router = APIRouter(prefix='/savings', tags=['savings'])

@router.get('/')
def index():
    return {{ "endpoint": "savings", "status": "ok" }}
