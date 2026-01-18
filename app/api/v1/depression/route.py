from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest,DepressionUpdate
router = APIRouter()


@router.post('/depression' , tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return get_depression()
@router.get('/searh' , tags=['Depression'])
def assess_depression(data: DepressionUpdate):
    return get_depression()