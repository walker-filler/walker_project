from ninja import Schema


class ProductSchema(Schema):
    item: str
    stock: int
