# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel

# Define your data model
class Item(BaseModel):
    id: int
    name: str
    description: str

# Create a FastAPI instance
app = FastAPI()

# In-memory database (a simple dictionary)
db = {}

# CRUD Operations

# Create an item
@app.post("/items/")
def create_item(item: Item):
    db[item.id] = item
    return item

# Read an item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return db.get(item_id)

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in db:
        db[item_id] = item
        return item
    return {"error": "Item not found"}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in db:
        del db[item_id]
        return {"message": "Item deleted"}
    return {"error": "Item not found"}

# Running the App
# To run the app, use the command: uvicorn main:app --reload
