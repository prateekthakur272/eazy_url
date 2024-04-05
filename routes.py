from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from database import get_db_session
from sqlalchemy.orm import Session
from models import ShortUrl
from utils import get_short_url, validate_url 
import uuid
from fastapi.exceptions import HTTPException
from fastapi import status


router = APIRouter()

@router.post('/', response_class=JSONResponse)
async def generate_short_url(url:str = Body(embed=True), session:Session = Depends(get_db_session)):
    if not validate_url(url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='invalid url')
    short_url = ShortUrl(url=url)
    session.add(short_url)
    session.commit()
    session.refresh(short_url)
    return {'short_url':get_short_url(short_url.id)}

@router.get('/{id}')
def open_url(id:str, session:Session = Depends(get_db_session)):
    try:
        url = session.query(ShortUrl).filter(ShortUrl.id == uuid.UUID(id)).first()
        if(not url):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return {'url':url.url}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)