import uuid
from flask import request
from flask.view import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

blp = Blueprint('stores',__name__, description="operation on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(cls,store_id):
        try:
            return stores[store_id]

        except KeyError:
            abort(404, message="key not found")
    
    def delete(cls,store_id):
        try:
            del stores[store_id]
        except KeyError:
            abort(404, message="store not found")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(cls):
        return {"stores": list(stores.values())}
    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(cls,store_data): 
        for store in stores.values():
            if store_data['name'] == store['name']:
                abort(400, message="Bad request, store already exist")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store
