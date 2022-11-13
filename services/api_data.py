from typing import Optional
import httpx
from Models.Character_model import CharacterModel as model

async def get_characterByid(characterId: int) -> Optional[model]:
    url = f"https://rickandmortyapi.com/api/character/{characterId}"
    async with httpx.AsyncClient() as client:
        response : httpx.Response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        character = model(**data)
        return character


