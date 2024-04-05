from settings import get_settings

settings =  get_settings()

def get_short_url(id:str) -> str:
    return f'{settings.BASE_URL}/{id}'