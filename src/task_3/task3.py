from fastapi import APIRouter, Query
router = APIRouter()

def concat_words(words:list[str]) -> str:
    letters = [word[i] for i, word in enumerate(words)]
    return ''.join(letters)

@router.get("")
async def join_words_letters(q: list[str] = Query(...)):
    return {"message": concat_words(q)}