from flask import Flask, request
from db import stores,items
from flask_smorest import abort
app = Flask(__name__)
import uuid

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request, ensure 'name' is included in json payload")
    for store in stores.values():
        if store_data['name'] == store['name']:
            abort(400, message="Bad request, store already exist")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if ("name" not in item_data or
        "store_id" not in item_data or
        "price" not in item_data):
        abort(400, message="Bad request, Ensure 'store_id' ,'name', 'price' are included in json payload")

    if item_data["store_id"] not in stores:
        abort (404, message="store not found")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    item[item_id]= item
    return item

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return item[item_id]
    except KeyError:
        abort(404, message ="store not found")

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:

        return stores[store_id]
    except KeyError:

        abort(404, message="Store not found.")

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "store was deleted"}
    except KeyError:
        abort(404, message="store not found")

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del item[item_id]
        return {"message":"item was deleted"}
    except KeyError:
        abort(404,message="item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(400, message="Bad request, ensure 'name' or 'price' is added in json payload")
    try:
        item = items[item_id]
        item |= item_data

        return item
    except KeyError:
        abort(404, message="item not found") 