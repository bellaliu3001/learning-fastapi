from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"},
    {"item_name": "123"},
    {"item_name": "234"},
    {"item_name": "345"},
    {"item_name": "456"},
    {"item_name": "567"},
    {"item_name": "678"},
    {"item_name": "789"},
    {"item_name": "987"},
    {"item_name": "876"},
    {"item_name": "765"},
    {"item_name": "654"},
    {"item_name": "543"},
    {"item_name": "432"},
    {"item_name": "321"},
    {"item_name": "210"},
    {"item_name": "111"},
    {"item_name": "222"},
]


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)