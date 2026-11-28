from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Mini projekat 3 API")
db = {}

class Item(BaseModel):
    name: str = Field(..., min_length=2, description="Naziv predmeta")
    price: float = Field(..., gt=0, description="Cena mora biti veca od 0")
    quantity: int = Field(default=1, ge=1, description="Kolicina mora biti najmanje 1")

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item_id] = item
    return {"item_id": item_id, "item": item}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]
