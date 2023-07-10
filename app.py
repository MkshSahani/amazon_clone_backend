from fastapi import FastAPI 
from users.index import user_index

app = FastAPI()

app.include_router(user_index)

@app.get(path="/")
async def tet_get():
    return {
        'work': True
    }