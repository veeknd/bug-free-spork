from marshmallow import Schema, fields

class PlainItemScheme(Scheme):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreScheme(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreScheme(), dump_only=True)

class ItemUpdateSchema(Schema):
    name = fiends.Str()
    price = fields.Float()


class StoreSchema(PlainStoreSchemeSchema):
    items = fields.List(fields.Nested(PlainItemScheme()), dump_only=True)