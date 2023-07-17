from flask import Flask, request
from db import stores,items
app = Flask(__name__)
import uuid

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message":"store not found"}, 404
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    item[item_id]= item

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_store(item_id):
    try:
        return item[item_id]
    except KeyError:    
        return {"message": "store not found"},404
