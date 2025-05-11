
from fastapi import APIRouter
router = APIRouter(prefix='/wallets', tags=['wallets'])

@router.get('/')
def index():
    return {{ "endpoint": "wallets", "status": "ok" }}
